<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50;
        }
        .box {
            border: 1 solid #ccc;
            padding: 20;
            width: 300;
            margin: auto;
            border-radius: 10;
        }
        input {
            margin: 10;
            padding: 8;
            width: 80%;
        }
        button {
            padding: 10, 20;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>BMI Calculator</h2>

    <input type="number" id="weight" placeholder="Enter weight (kg)">
    <input type="number" id="height" placeholder="Enter height (m)">

    <br>
    <button onclick="calculateBMI()">Calculate</button>

    <h3 id="result"></h3>
</div>

<script>
function calculateBMI() {
    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value;

    let bmi = weight / (height * height);

    let category = "";

    if (bmi < 18.5) category = "Underweight";
    else if (bmi < 25) category = "Normal";
    else if (bmi < 30) category = "Overweight";
    else category = "Obese";

    document.getElementById("result").innerHTML =
        "BMI: " + bmi.toFixed(2) + " (" + category + ")";
}
</script>

</body>
</html>
