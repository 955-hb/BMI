# Schreibe ein Programm welches die Größe und Gewicht einer Person (mittels input) abfragt
# und auf dieser Basis den BMI berechnet und ausgibt.
# Formel = (Gewicht in kg) / (Körpergröße im m)^2


print('Berechne deinen BMI-Wert')

age = input('Wie alt bist du?')
height_str = input('Wie groß bist du? (in m)')
weight_str = input('Wie schwer bist du? (in kg)')

height = float(height_str.replace(",","."))
weight = float(weight_str.replace(",","."))

result_bmi = weight / height **2

bmi = round(result_bmi, 2)
print('Mit Ihren alter von ' + str(age) + ' haben Sie einen BMI-Wert von: ' + str(bmi) + '!')

if bmi < 16:
    print('Sie haben ein kritisches Untergewicht!')
elif bmi >= 16 and bmi <= 18.5:
    print('Sie haben leichtes Untergewicht!')
elif bmi >= 18.5 and bmi <= 25:
    print('Sie haben ein Normalgewicht!')
elif bmi >= 25 and bmi <= 30:
    print('Sie haben leichtes Übergewicht!')
elif bmi > 30:
    print('Sie haben erhöhtes Übergewicht!')

input('drücken Sie eine beliebige Taste zum Beenden des Programmes!')


