from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/model',methods=['POST'])
def model():
    model1 = pickle.load(open('Model_Jay.pkl', 'rb'))
    model2 = pickle.load(open('Model_JINI.pkl', 'rb'))
    
    final_data = [np.array([x for x in request.form.values()])]
    prediction1 = model1.predict([final_data[0][:7]])
    prediction2 = model2.predict(final_data)

    if (prediction1[0] == 1):
        recommendation1 = "These customers should be given schemes accordingly to increase their purchase which will indirectly increase oneoff purchase and installment purchases."
        insight1 = "Customers of cluster 1 have a pretty good credit limit and balance but these customers have a very low oneoff purchase and purchases in comparison to cash advance. This means they take more cash advance and spend less through purchasing."
    elif (prediction1[0] == 0):
        insight1 = "Credit limit of customers of cluster 0 is lowest amongst all. These customers have a low balance but they have quite good purchase and installment purchases."
        recommendation1 = "These customers can be given discount offer on buying things so that they will start using their credit card more frequently."
    elif (prediction1[0] == 2):
        recommendation1 = "These customers should be encouraged by giving schemes to spend more and to increase the balance by keeping a minimum balance."
        insight1 = "These customers have a good credit limit but their balance, oneoff urchase, purchases, installment purchases is very low."
    elif (prediction1[0] == 3):
        recommendation1 = "These customers should be encouraged to keep decent balance in their account by keeping a minimum balance rule."
        insight1 = "These customers have the highest credit limit and oneoff purchase followed by purchases and installment purchases. They have highest payment of all clusters."
    else:
        insight1 = "Error"
        recommendation1 = "Error"

    if (prediction2[0] == 0):
        insight2 = "Their Balance is less but they purchase without cash advances. They prefer instalments for purchases and make sure to repay the same at time."
        recommendation2 = "They are good customers even with less balance they purchase stuff. So give them schemes of discounts on some expensive products so that they are attracted to buy more stuff since they are frequent buyers . They are quite in number so the company should surely focus on them."
    elif (prediction2[0] == 1):
        insight2 = "Rich people with a lot of balance but not frequent buyers. Take a lot of cash advance to purchase expensive stuff."
        recommendation2 = "Come up with schemes that provide discounts on both expensive as well as ordinary items."
    elif (prediction2[0] == 2):
        insight2 = "Cream customer who have been there for a long time now and even do a lot of purchases. Take minimal cash advance and installments to do purchases."
        recommendation2 = "Make sure not to lose them .Come up with schemes which benefits them the most."
    elif (prediction2[0] == 3):
        insight2 = "Less balance and not much purchases. They don’t even take cash advance and installments to do purchases."
        recommendation2 = "Focus a lot on them as they are a lot in number and aren't giving much profits. Come up with the schemes that make them active users."
    else:
        insight2 = "Error"
        recommendation2 = "Error"

    return render_template('index.html', prediction1=f'This customer belongs to cluster {prediction1[0]}', insight1=insight1, recommendation1=recommendation1, prediction2=f'This customer belongs to cluster {prediction2[0]}', insight2=insight2, recommendation2=recommendation2)

if __name__ == "__main__":
    app.run(debug=True)