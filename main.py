from flask import Flask, session, render_template, json, request, jsonify
import numpy as np
from array import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

#@app.route('/showSignUp')
#def showSignUp():
#	return render_template('signUp.html')

deadPercent = array('f', [])
livePercent = array('f', [])
elastiCity = array('f', [])
duration = array('f', [])
intensity = array('f', [])
extruder1 = array('f', [])
extruder2 = array('f', [])
layerHeight = array('f', [])
layerNum = array('f', [])
wellplate = array('f', [])

    

@app.route("/output",methods=['POST'])
def output():
	flag = 0
	req = request.json
	_email = req['email']
	with open('bioprint-data.json') as json_data:
		data = json.load(json_data)
	for datum in data:
		for k,v in datum.items():
			if k == "user_info" and v['email'] == str(_email):
				flag = 1
				deadPercent.append(datum['print_data']['deadPercent'])
				livePercent.append(datum['print_data']['livePercent'])
				elastiCity.append(datum['print_data']['elasticity'])
				duration.append(datum['print_info']['crosslinking']['cl_duration'])
				intensity.append(datum['print_info']['crosslinking']['cl_intensity'])
				extruder1.append(datum['print_info']['pressure']['extruder1'])
				extruder2.append(datum['print_info']['pressure']['extruder2'])
				layerHeight.append(datum['print_info']['resolution']['layerHeight'])
				layerNum.append(datum['print_info']['resolution']['layerNum'])
				wellplate.append(datum['print_info']['wellplate'])
				#print("Code : {0}, Value : {1}".format(k, v))

	# print info 
	print reduce(lambda x, y: x + y, deadPercent) / len(deadPercent)
	print reduce(lambda x, y: x + y, livePercent) / len(livePercent)
	print reduce(lambda x, y: x + y, elastiCity) / len(elastiCity)
    
    # print data cross linking
	print reduce(lambda x, y: x + y, duration) / len(duration)
	print reduce(lambda x, y: x + y, intensity) / len(intensity)

    # print data Pressure
	print reduce(lambda x, y: x + y, extruder1) / len(extruder1)
	print reduce(lambda x, y: x + y, extruder2) / len(extruder2)

    # print data Resolution 
	print reduce(lambda x, y: x + y, layerHeight) / len(layerHeight)
	print reduce(lambda x, y: x + y, layerNum) / len(layerNum)

     # print data wellplate
	print reduce(lambda x, y: x + y, wellplate) / len(wellplate)
	
	#print elastiCity
	#print deadPercent
	#print duration
	#print intensity
	#print extruder1
	#print extruder2
	#print layerHeight
	#print layerNum
	#print wellplate

	values = '[["Range", "Dead Percent" , "Live Percent", "Elasticity",{ "role": "annotation" } ],'
	valueToAdd = values + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in deadPercent)` + ',' + `sum(0 <= x <= 10 for x in livePercent)`+ ',' + `sum(0 <= x <= 10 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in deadPercent)` + ',' + `sum(11 <= x <= 20 for x in livePercent)` + ',' + `sum(11 <= x <= 20 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in deadPercent)` + ',' + `sum(21 <= x <= 30 for x in livePercent)` + ',' + `sum(21 <= x <= 30 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in deadPercent)` + ',' + `sum(31 <= x <= 40 for x in livePercent)` + ',' + `sum(31 <= x <= 40 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in deadPercent)` + ',' + `sum(41 <= x <= 50 for x in livePercent)` + ',' + `sum(41 <= x <= 50 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in deadPercent)` + ',' + `sum(51 <= x <= 60 for x in livePercent)` + ',' + `sum(51 <= x <= 60 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in deadPercent)` + ',' + `sum(61 <= x <= 70 for x in livePercent)` + ',' + `sum(61 <= x <= 70 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in deadPercent)` + ',' + `sum(71 <= x <= 80 for x in livePercent)` + ',' + `sum(71 <= x <= 80 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in deadPercent)` + ',' + `sum(81 <= x <= 90 for x in livePercent)` + ',' + `sum(81 <= x <= 90 for x in elastiCity)` + ', ""],'
	valueToAdd = valueToAdd + '["' + "91-100" + '",' + `sum(91 <= x <= 100 for x in deadPercent)` + ',' + `sum(91 <= x <= 100 for x in livePercent)`+ ',' + `sum(91 <= x <= 100 for x in elastiCity)` + ', ""]]'
   	#print valueToAdd
	
	# chart for print info Pressure
	
	values1 = '[["Range", "Extruder 1" , "Extruder 2",{ "role": "annotation" } ],'
	valueToAdd1 = values1 + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in extruder1)` + ',' + `sum(0 <= x <= 10 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in extruder1)` + ',' + `sum(11 <= x <= 20 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in extruder1)` + ',' + `sum(21 <= x <= 30 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in extruder1)` + ',' + `sum(31 <= x <= 40 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in extruder1)` + ',' + `sum(41 <= x <= 50 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in extruder1)` + ',' + `sum(51 <= x <= 60 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in extruder1)` + ',' + `sum(61 <= x <= 70 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in extruder1)` + ',' + `sum(71 <= x <= 80 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in extruder1)` + ',' + `sum(81 <= x <= 90 for x in extruder2)` + ', ""],'
	valueToAdd1 = valueToAdd1 + '["' + "91-100" + '",' + `sum(91 <= x <= 100 for x in extruder1)` + ',' + `sum(91 <= x <= 100 for x in extruder2)`+ ', ""]]'


	# Resolution Layer Height <less than 1 
	
	values4 = '[["Range", "Layer Height" ,{ "role": "annotation" } ],'
	valueToAdd4 = values4 + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in layerHeight)` + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in layerHeight)` + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in layerHeight)`  + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in layerHeight)` + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in layerHeight)` + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in layerHeight)` +  ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in layerHeight)` +  ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in layerHeight)` + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in layerHeight)`  + ', ""],'
	valueToAdd4 = valueToAdd4 + '["' + "91-100" + '",' + `sum(91 <= x <= 100 for x in layerHeight)` + ', ""]]'


	#Resolution Layer Num <less than 50
	values2 = '[["Range", "Layer Num",{ "role": "annotation" } ],'
	valueToAdd2 = values2 + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in layerNum)` + ', ""],'
	valueToAdd2 = valueToAdd2 + '["' + "91-100" + '",'+ `sum(91 <= x <= 100 for x in layerNum)`+ ', ""]]'


	#WellPlate
	values3= '[["Range", "Wellplate", { "role": "annotation" } ],'
	valueToAdd3=values3 + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in wellplate)` + ', ""],'
	valueToAdd3=valueToAdd3 + '["' + "91-100" + '",' + `sum(91 <= x <= 100 for x in wellplate)` + ', ""]]'


	values5= '[["Range", "Cl Intensity", { "role": "annotation" } ],'
	valueToAdd5=values5 + '["' + "0-10" + '",' + `sum(0 <= x <= 10 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "11-20" + '",' + `sum(11 <= x <= 20 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "21-30" + '",' + `sum(21 <= x <= 30 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "31-40" + '",' + `sum(31 <= x <= 40 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "41-50" + '",' + `sum(41 <= x <= 50 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "51-60" + '",' + `sum(51 <= x <= 60 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "61-70" + '",' + `sum(61 <= x <= 70 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "71-80" + '",' + `sum(71 <= x <= 80 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "81-90" + '",' + `sum(81 <= x <= 90 for x in intensity)` + ', ""],'
	valueToAdd5=valueToAdd5 + '["' + "91-100" + '",' + `sum(91 <= x <= 100 for x in intensity)` + ', ""]]'


	if(flag == 1):
		return jsonify({'ColumnChartValues' : valueToAdd, 'ColumnChartValues1' : valueToAdd1, 'ColumnChartValues2' : valueToAdd2, 'ColumnChartValues3' : valueToAdd3, 'ColumnChartValues4': valueToAdd4, 'ColumnChartValues5': valueToAdd5})
	else:
		return jsonify({'ColumnChartValues' : "null"})
	

if __name__ == "__main__":
	app.run()

    

