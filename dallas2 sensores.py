import machine, onewire, ds18x20, time

# Configuración de pines
ds_sensor1 = ds18x20.DS18X20(onewire.OneWire(machine.Pin(16)))
ds_sensor2 = ds18x20.DS18X20(onewire.OneWire(machine.Pin(27)))

# Escaneo inicial
roms1 = ds_sensor1.scan()
roms2 = ds_sensor2.scan()

# Validar que existan sensores para evitar errores en el loop
if not roms1 or not roms2:
    print("Error: Asegúrate de tener un sensor en cada pin.")

while True:
    try:
        # Iniciar conversión
        ds_sensor1.convert_temp()
        ds_sensor2.convert_temp()
        
        # Espera necesaria para la lectura
        time.sleep_ms(750)
        
        # Suponiendo que hay un sensor por pin, tomamos el primero de cada lista [0]
        temp1 = ds_sensor1.read_temp(roms1[0])
        temp2 = ds_sensor2.read_temp(roms2[0])
        
        # Formato para el Plotter: "valor1, valor2"
        # Thonny reconocerá automáticamente esto como dos líneas diferentes
        print(f"{temp1:.2f}, {temp2:.2f}")
        
    except Exception as e:
        # En caso de error de lectura, imprimimos ceros para no romper la gráfica
        print("0.00, 0.00")
        
    time.sleep(1)