import joblib
import tkinter as tk

from sklearn.datasets import data


def clicked():
    """Specify what the app does when the button is clicked"""
    name = txt1.get()
    pclass = float(txt2.get())
    sex = 0 if txt3.get() == "male" else 1
    age = float(txt4.get())
    ss = float(txt5.get())
    pc = float(txt6.get())
    fare = float(txt7.get())
    passenger_to_classify = [[pclass, sex, age, ss, pc, fare]]
    print(passenger_to_classify)

    prediction = titanic_knn_model.predict(passenger_to_classify)
    print(prediction)
    classes = ["didn't survive", "survived"]
    label = classes[prediction[0]]

    confidence = titanic_knn_model.predict_proba(passenger_to_classify)
    res = "I'm {}% sure that {} {} the sinking\n".format(confidence*100, name, label)
    print(res)


# load the machine learning trained model
titanic_knn_model = joblib.load('titanic.csv')
# create a new window and set properties
window = tk.Tk()
window.title("Titanic")
window.geometry('400x230')
window['bg'] = 'grey'

# labels and text entries to ask the user for the input data
lbl1 = tk.Label(window, text="Passenger Name",
                foreground="white",  # Set the text color to white
                background="grey"  # Set the background color to black
                )
lbl1.grid(column=0, row=0)
txt1 = tk.Entry(window, width=20)
txt1.grid(column=1, row=0)
lbl2 = tk.Label(window, text="Class", fg="white",  bg="grey")
lbl2.grid(column=0, row=1)
txt2 = tk.Entry(window, width=20)
txt2.grid(column=1, row=1)
lbl3 = tk.Label(window, text="Sex (male/female)", fg="white",  bg="grey")
lbl3.grid(column=0, row=2)
txt3 = tk.Entry(window, width=20)
txt3.grid(column=1, row=2)
lbl4 = tk.Label(window, text="Age", fg="white",  bg="grey")
lbl4.grid(column=0, row=3)
txt4 = tk.Entry(window, width=20)
txt4.grid(column=1, row=3)
lbl5 = tk.Label(window, text="Siblings/Spouses Aboard", fg="white",  bg="grey")
lbl5.grid(column=0, row=4)
txt5 = tk.Entry(window, width=20)
txt5.grid(column=1, row=4)
lbl6 = tk.Label(window, text="Parents/Children Aboard", fg="white",  bg="grey")
lbl6.grid(column=0, row=5)
txt6 = tk.Entry(window, width=20)
txt6.grid(column=1, row=5)
lbl7 = tk.Label(window, text="Fare", fg="white",  bg="grey")
lbl7.grid(column=0, row=6)
txt7 = tk.Entry(window, width=20)
txt7.grid(column=1, row=6)

# create a button to classify and make prediction
btn = tk.Button(window, text="Predict", command=clicked)
btn.grid(column=1, row=7)

window.mainloop()
