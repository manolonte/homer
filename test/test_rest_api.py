import requests
res = requests.post('http://localhost:5000/set_device_property/enchufe_esquina_salon', json={"property":"state","value":"ON"})
if res.ok:
    print(res.json())
res = requests.get('http://localhost:5000/get_device_state/enchufe_esquina_salon')
if res.ok:
    print(res.json())
res = requests.post('http://localhost:5000/set_device_property/enchufe_esquina_salon', json={"property":"state","value":"OFF"})
if res.ok:
    print(res.json())
res = requests.get('http://localhost:5000/get_device_state/enchufe_esquina_salon')
if res.ok:
    print(res.json())