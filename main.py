from pyscript import document, display


x = "This is an editable copy. Use this environment every time we have discussions for our demo."




display(x, target="output1")

def CheckNum(e):
    num_bers = ["1", "2", "5", "6", "9"]

    num1 = document.getElementById("num1").value

    name = document.getElementById("name").value

    comfirm = num1 in num_bers

    message = (f'sorry {name}, your number is gone forever', f'Yay! {name}, everybody is a ren worshipper.')

    document.getElementById("output1").innerHTML = message[comfirm]

    