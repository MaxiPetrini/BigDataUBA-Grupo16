"""
Este archivo contiene todos los mapeos de strings utilizados en el procesamiento de datos.
"""

STRING_MAPPINGS = {
    'REGION': {  # Código de Región
        '43': 'Pampeana',
    },
    'H15': {  # Entrevista individual realizada
        '1': 'Sí ',
        '2': 'No'
    },
    'CAT_OCUP': {  # Categoría ocupacional
        "1": "Patrón",
        "2": "Cuenta propia",
        "3": "Obrero o empleado",
        "4": "Trabajador familiar sin remuneración",
        "9": "Ns/Nr"
    },
    'CH04': {  # Sexo
        '1': 'Varón',
        '2': 'Mujer',
    },
    'AGLOMERADO': {  # Codigo de Aglomerado
        '2': "Gran La Plata",
        '3': "Bahía Blanca - Cerri",
        '4': "Gran Rosario",
        '5': "Gran Santa Fé",
        '6': "Gran Paraná",
        '7': "Posadas",
        '8': "Gran Resistencia",
        '9': "Cdro. Rivadavia – Rada Tilly",
        '10': "Gran Mendoza",
        '12': "Corrientes",
        '13': "Gran Córdoba",
        '14': "Concordia",
        '15': "Formosa",
        '17': "Neuquén – Plottier",
        '18': "S.del Estero - La Banda",
        '19': "Jujuy - Palpalá",
        '20': "Río Gallegos",
        '22': "Gran Catamarca",
        '23': "Salta",
        '25': "La Rioja",
        '26': "San Luis - El Chorrillo",
        '27': "Gran San Juan",
        '29': "Gran Tucumán - T. Viejo",
        '30': "Santa Rosa - Toay",
        '31': "Ushuaia - Río Grande",
        '32': "Ciudad de Buenos Aires",
        '33': "Partidos del GBA",
        '34': "Mar del Plata - Batán",
        '36': "Río Cuarto",
        '38': 'San Nicolás – Villa Constitución',
        '91': 'Rawson – Trelew',
        '93': 'Viedma – Carmen de Patagones'
    },
    'CH03': {  # Relación de Parentesco
        "1": "Jefe",
        "2": "Cónyuge/Pareja",
        '3': "Hijo/Hijastro",
        "4": "Yerno/Nuera",
        "5": "Nieto",
        "6": "Madre/Padre",
        "7": "Suegro",
        "8": "Hermano",
        "9": "Otros familiares",
        "10": "No familiares",
    },
    'CH07': {  # ¿Actualmente está...
        '1': 'Unido',
        '2': 'Casado',
        '3': 'Separado o divorciado',
        '4': 'Viudo',
        '5': 'Soltero'
    },
    'CH09': {  # ¿Sabe leer y escribir?
        '1': 'Sí',
        '2': 'No',
        '3': 'Menor de 2 años'
    },
    'CH10': {  # ¿Asiste o asistió a algún establecimiento educativo?
        '1': 'Sí, asiste',
        '2': 'No asiste, pero asistió',
        '3': 'Nunca asistió'
    },
    'CH11': {  # Ese establecimiento es
        '1': 'Público',
        '2': 'Privado',
        '9': 'Ns./Nr.'
    },
    'NIVEL_ED': {  # NIVEL EDUCATIVO
        '1': 'Primario incompleto (incluye educación especial)',
        '2': 'Primario completo',
        '3': 'Secundario incompleto',
        '4': 'Secundario completo',
        '5': 'Superior universitario incompleto',
        '6': 'Superior universitario completo',
        '7': 'Sin instrucción',
        '9': 'Ns/Nr'
    },
    'CH08': {  # ¿Tiene algún tipo de cobertura médica?
        '1': 'Obra social (incluye PAMI)',
        '2': 'Mutual/Prepaga/Servicio de emergencia',
        '3': 'Planes y seguros públicos',
        '4': 'No paga ni le descuentan',
        '9': 'Ns./Nr.',
        '12': 'Obra social y mutual/prepaga/servicio de emergencia',
        '13': 'Obra social y planes y seguros públicos',
        '23': 'Mutual/prepaga/servicio de emergencia/planes y seguros públi',
        '123': 'Obra social, mutual/prepaga/servicio de emergencia y planes'
    },
    'CH16': {  # Dónde vivía hace 5 años?
        '1': 'En esta localidad',
        '2': 'En otra localidad de esta provincia',
        '3': 'En otra provincia (especificar)',
        '4': 'En un país limítrofe',
        '5': 'En otro país',
        '6': 'No había nacido',
        '9': 'Ns/Nr'
    },
    'ESTADO': {  # Condición de actividad
        '0': 'Entrevista individual no realizada (no respuesta al cuestion',
        '1': 'Ocupado',
        '2': 'Desocupado',
        '3': 'Inactivo',
        '4': 'Menor de 10 años'
    },
    'CAT_INAC': {  # Categoría de inactividad
        '1': 'Jubilado/pensionado',
        '2': 'Rentista',
        '3': 'Estudiante',
        '4': 'Ama de casa',
        '5': 'Menor de 6 años',
        '6': 'Discapacitado',
        '7': 'Otros'
    },
    'CH12': {  # ¿Cuál es el nivel más alto que cursa o cursó?
        '1': 'Jardín/Preescolar',
        '2': 'Primario',
        '3': 'EGB',
        '4': 'Secundario',
        '5': 'Polimodal',
        '6': 'Terciario',
        '7': 'Universitario',
        '8': 'Posgrado universitario',
        '9': 'Educación especial',
        '0': 'No tiene',
        '99': 'Ns/Nr'
    },
    'MAS_500': {  # Aglomerados según tamaño
        'N': 'Conjunto de aglomerados de menos de 500.000 habitantes',
        'S': 'Conjunto de aglomerados de 500.000 y más habitantes'
    },
    'CH14': {  # Último año que aprobó
        '00': 0,
        '01': 1,
        '02': 2,
        '03': 3,
        '04': 4,
        '05': 5,
        '06': 6,
        '07': 7,
        '08': 8,
        '09': 9,
        '98': 0,  # Educación especial
        '99': 0   # Ns/Nr
    },
    'TRIMESTRE': {  # Número de trimestre
        '1': '1er. Trimestre',
        '2': '2do. Trimestre',
        '3': '3er. Trimestre',
        '4': '4to. Trimestre'
    },
    'CH13': {  # ¿Finalizó ese nivel?
        '1': 'Sí',
        '2': 'No',
        '0': 'Ns/Nr',
        '9': 'Ns/Nr'
    },
    'CH15': {  # ¿Dónde nació?
        '1': 'En esta localidad',
        '2': 'En otra localidad de esta provincia',
        '3': 'En otra provincia (especificar)',
        '4': 'En un país limítrofe (especificar: Brasil, Bolivia, Chile, Paraguay, Uruguay)',
        '5': 'En otro país (especificar)',
        '9': 'Ns/Nr'
    },
    'PP02H': {  # ¿Buscó trabajo en los últimos 12 meses?
        '1': 'Sí',
        '2': 'No'
    },
    'PP02I': {  # ¿Trabajó en los últimos 12 meses?
        '1': 'Sí',
        '2': 'No'
    },
    'PP03I': {  # En los últimos treinta días, ¿buscó trabajar más horas?
        '1': 'Sí',
        '2': 'No',
        '9': 'Ns./Nr.'
    },
    'PP03J': {  # ¿Estuvo buscando algún empleo/ocupación/actividad?
        '1': 'Sí',
        '2': 'No',
        '9': 'Ns./Nr.'
    },
    'INTENSI': {  # Intensidad de la ocupación
        '1': 'Subocupación horaria Demandante',
        '2': 'Subocupación horaria No Demandante',
        '3': 'Ocupación plena',
        '4': 'Sobreocupación horaria',
        '5': 'Ocupado que no trabajó en la semana',
        '9': 'Ns./Nr.'
    }
} 