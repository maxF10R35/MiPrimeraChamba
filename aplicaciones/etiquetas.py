# Diccionario SINCO 2019 (Estructura Jerárquica: División -> Grupo -> Subgrupo)

SINCO = {
    '1': {
        'nombre': 'Funcionarios, directores y jefes',
        'grupos': {
            '11': {
                'nombre': 'Funcionarios y altas autoridades de los sectores público, privado y social',
                'subgrupos': {
                    '111': 'Funcionarios, legisladores y autoridades gubernamentales',
                    '112': 'Presidentes y directores generales',
                    '113': 'Directores de organizaciones políticas, sindicales y civiles'
                }
            },
            '12': {
                'nombre': 'Directores y gerentes en servicios financieros, legales, administrativos y sociales',
                'subgrupos': {
                    '121': 'Directores y gerentes en servicios financieros y administrativos',
                    '122': 'Directores y gerentes en servicios de salud, enseñanza y sociales'
                }
            },
            '13': {
                'nombre': 'Directores y gerentes en producción, tecnología y transporte',
                'subgrupos': {
                    '131': 'Directores y gerentes en producción agropecuaria, industrial, construcción y mantenimiento',
                    '132': 'Directores y gerentes en informática, telecomunicaciones, transporte y en investigación y desarrollo tecnológico'
                }
            },
            '14': {
                'nombre': 'Directores y gerentes de ventas, restaurantes, hoteles y otros establecimientos',
                'subgrupos': {
                    '141': 'Directores y gerentes de ventas, restaurantes y hoteles',
                    '142': 'Directores y gerentes de museos, cines y otros establecimientos'
                }
            },
            '15': {
                'nombre': 'Coordinadores y jefes de área en servicios financieros, administrativos y sociales',
                'subgrupos': {
                    '151': 'Coordinadores y jefes de área en servicios financieros y administrativos',
                    '152': 'Coordinadores y jefes de área en servicios de salud, enseñanza, sociales y jueces calificadores'
                }
            },
            '16': {
                'nombre': 'Coordinadores y jefes de área en producción y tecnología',
                'subgrupos': {
                    '161': 'Coordinadores y jefes de área en producción agropecuaria, industrial, construcción y mantenimiento',
                    '162': 'Coordinadores y jefes de área en informática, telecomunicaciones, transporte y en investigación y desarrollo tecnológico'
                }
            },
            '17': {
                'nombre': 'Coordinadores y jefes de área de ventas, restaurantes, hoteles y otros establecimientos',
                'subgrupos': {
                    '171': 'Coordinadores y jefes de área de ventas, restaurantes y hoteles',
                    '172': 'Coordinadores y jefes de área en museos, cines y otros establecimientos'
                }
            },
            '19': {
                'nombre': 'Otros directores, funcionarios, gerentes, coordinadores y jefes de área, no clasificados anteriormente',
                'subgrupos': {
                    '199': 'Otros directores, funcionarios, gerentes, coordinadores y jefes de área, no clasificados anteriormente'
                }
            }
        }
    },
    '2': {
        'nombre': 'Profesionistas y técnicos',
        'grupos': {
            '21': {
                'nombre': 'Profesionistas en ciencias económico-administrativas, ciencias sociales, humanistas y en artes',
                'subgrupos': {
                    '211': 'Administradores y mercadólogos',
                    '212': 'Contadores, auditores y profesionistas en finanzas',
                    '213': 'Investigadores y profesionistas en ciencias sociales',
                    '214': 'Investigadores y profesionistas en ciencias humanistas',
                    '215': 'Escritores, periodistas y traductores',
                    '216': 'Pintores, diseñadores y dibujantes artísticos, escultores y escenógrafos',
                    '217': 'Artistas interpretativos'
                }
            },
            '22': {
                'nombre': 'Investigadores y profesionistas en ciencias exactas, biológicas, ingeniería, informática y en telecomunicaciones',
                'subgrupos': {
                    '221': 'Investigadores y profesionistas en física, matemáticas, estadística y actuaría',
                    '222': 'Investigadores y profesionistas en ciencias biológicas, químicas y del medio ambiente',
                    '223': 'Profesionistas en ciencias agronómicas',
                    '224': 'Ingenieros eléctricos y en electrónica',
                    '225': 'Ingenieros químicos, mecánicos, industriales, mineros y metalúrgicos',
                    '226': 'Ingenieros civiles, topógrafos y arquitectos',
                    '227': 'Investigadores y profesionistas en sistemas computacionales',
                    '228': 'Ingenieros en comunicaciones y telecomunicaciones'
                }
            },
            '23': {
                'nombre': 'Profesores y especialistas en docencia',
                'subgrupos': {
                    '231': 'Supervisores educativos y especialistas en ciencias de la educación',
                    '232': 'Profesores de nivel medio y superior',
                    '233': 'Profesores de nivel básico',
                    '234': 'Profesores de enseñanza especial',
                    '239': 'Otros profesores y especialistas en docencia, no clasificados anteriormente'
                }
            },
            '24': {
                'nombre': 'Médicos, enfermeras y otros especialistas en salud',
                'subgrupos': {
                    '241': 'Médicos generales y dentistas',
                    '242': 'Médicos especialistas',
                    '243': 'Otros especialistas en salud'
                }
            },
            '25': {
                'nombre': 'Auxiliares y técnicos en ciencias económico-administrativas, ciencias sociales, humanistas y en artes',
                'subgrupos': {
                    '251': 'Auxiliares en administración, contabilidad y finanzas',
                    '252': 'Inspectores públicos',
                    '253': 'Auxiliares en ciencias sociales y humanistas',
                    '254': 'Diseñadores de modas, industriales, gráficos y decoradores de interiores',
                    '255': 'Locutores, animadores y payasos',
                    '256': 'Deportistas, entrenadores y árbitros'
                }
            },
            '26': {
                'nombre': 'Auxiliares y técnicos en ciencias exactas, biológicas, ingeniería, informática y en telecomunicaciones',
                'subgrupos': {
                    '261': 'Auxiliares y técnicos en ciencias físicas, matemáticas, biológicas, químicas, del medio ambiente y agronómicas',
                    '262': 'Auxiliares y técnicos industriales, topógrafos, mineros y dibujantes técnicos',
                    '263': 'Mecánicos y técnicos en mantenimiento y reparación de equipos mecánicos, vehículos de motor, instrumentos industriales y equipo de refrigeración',
                    '264': 'Técnicos eléctricos, en electrónica y de equipos en telecomunicaciones y electromecánicos',
                    '265': 'Auxiliares y técnicos en informática y en equipos de comunicaciones y grabación',
                    '266': 'Controladores de tráfico aéreo y de otros transportes'
                }
            },
            '27': {
                'nombre': 'Auxiliares y técnicos en educación, instructores y capacitadores',
                'subgrupos': {
                    '271': 'Auxiliares y técnicos en educación, instructores y capacitadores'
                }
            },
            '28': {
                'nombre': 'Enfermeras, técnicos en medicina y trabajadores de apoyo en salud',
                'subgrupos': {
                    '281': 'Enfermeras y técnicos en medicina',
                    '282': 'Trabajadores de apoyo en salud'
                }
            },
            '29': {
                'nombre': 'Otros profesionistas y técnicos no clasificados anteriormente',
                'subgrupos': {
                    '299': 'Otros profesionistas y técnicos no clasificados anteriormente'
                }
            }
        }
    },
    '3': {
        'nombre': 'Trabajadores auxiliares en actividades administrativas',
        'grupos': {
            '31': {
                'nombre': 'Supervisores de personal de apoyo administrativo, secretarias, capturistas, cajeros y trabajadores de control de archivo y transporte',
                'subgrupos': {
                    '310': 'Supervisores de secretarias, capturistas, cajeros y trabajadores de control de archivo y transporte',
                    '311': 'Secretarias, taquígrafos, mecanógrafos, capturistas de datos y operadores de máquinas de oficina',
                    '312': 'Cajeros, cobradores y pagadores',
                    '313': 'Trabajadores en archivo y control de almacén y bodega',
                    '314': 'Trabajadores en el control de la operación de transporte'
                }
            },
            '32': {
                'nombre': 'Supervisores y trabajadores que brindan y manejan información',
                'subgrupos': {
                    '320': 'Supervisores de trabajadores que brindan y manejan información',
                    '321': 'Recepcionistas, trabajadores que brindan información y telefonistas',
                    '322': 'Trabajadores en agencias de viajes e información turística',
                    '323': 'Encuestadores y codificadores'
                }
            },
            '39': {
                'nombre': 'Otros trabajadores auxiliares en actividades administrativas, no clasificados anteriormente',
                'subgrupos': {
                    '399': 'Otros trabajadores auxiliares en actividades administrativas, no clasificados anteriormente'
                }
            }
        }
    },
    '4': {
        'nombre': 'Comerciantes, empleados en ventas y agentes de ventas',
        'grupos': {
            '41': {
                'nombre': 'Comerciantes en establecimientos',
                'subgrupos': {
                    '411': 'Comerciantes en establecimientos'
                }
            },
            '42': {
                'nombre': 'Empleados de ventas en establecimientos',
                'subgrupos': {
                    '420': 'Encargados y supervisores de ventas de productos y de servicios financieros',
                    '421': 'Empleados de ventas y vendedores por teléfono',
                    '422': 'Agentes, representantes de ventas y vendedores por catálogo',
                    '423': 'Trabajadores en la promoción de ventas y modelos'
                }
            },
            '43': {
                'nombre': 'Trabajadores en servicios de alquiler',
                'subgrupos': {
                    '430': 'Supervisores en servicios de alquiler',
                    '431': 'Trabajadores en servicios de alquiler'
                }
            },
            '49': {
                'nombre': 'Otros comerciantes, empleados en ventas y agentes de ventas en establecimiento, no clasificados anteriormente',
                'subgrupos': {
                    '499': 'Otros comerciantes, empleados en ventas y agentes de ventas en establecimientos, no clasificados anteriormente'
                }
            }
        }
    },
    '5': {
        'nombre': 'Trabajadores en servicios personales y de vigilancia',
        'grupos': {
            '51': {
                'nombre': 'Trabajadores en la preparación y servicio de alimentos y bebidas, así como en servicios de esparcimiento y de hotelería',
                'subgrupos': {
                    '510': 'Supervisores en la preparación y servicio de alimentos y bebidas, así como en servicios de esparcimiento y de hotelería',
                    '511': 'Trabajadores en la preparación y servicio de alimentos y bebidas en establecimientos'
                }
            },
            '52': {
                'nombre': 'Trabajadores en cuidados personales y del hogar',
                'subgrupos': {
                    '520': 'Supervisores y encargados de trabajadores en cuidados personales y del hogar',
                    '521': 'Peluqueros, embellecedores y similares',
                    '522': 'Trabajadores en el cuidado de personas',
                    '523': 'Azafatas y sobrecargos',
                    '524': 'Jardineros',
                    '525': 'Trabajadores en otros servicios personales',
                    '529': 'Otros trabajadores en servicios personales no clasificados anteriormente'
                }
            },
            '53': {
                'nombre': 'Trabajadores en servicios de protección y vigilancia',
                'subgrupos': {
                    '530': 'Supervisores en servicios de protección y vigilancia',
                    '531': 'Trabajadores en servicios de protección y vigilancia'
                }
            },
            '54': {
                'nombre': 'Trabajadores de la Armada, Ejército y Fuerza Aérea',
                'subgrupos': {
                    '540': 'Supervisores de la Armada, Ejército y Fuerza Aérea',
                    '541': 'Trabajadores de la Armada, Ejército y Fuerza Aérea'
                }
            }
        }
    },
    '6': {
        'nombre': 'Trabajadores en actividades agrícolas, ganaderas, forestales, caza y pesca',
        'grupos': {
            '61': {
                'nombre': 'Trabajadores en actividades agrícolas y ganaderas',
                'subgrupos': {
                    '610': 'Supervisores, encargados y capataces agropecuarios',
                    '611': 'Trabajadores en actividades agrícolas',
                    '612': 'Trabajadores en actividades ganaderas y en la cría de animales',
                    '613': 'Trabajadores que combinan actividades agrícolas con ganaderas'
                }
            },
            '62': {
                'nombre': 'Trabajadores en actividades pesqueras, forestales, caza y similares',
                'subgrupos': {
                    '620': 'Supervisores, encargados y capataces de trabajadores en actividades pesqueras, acuícolas, forestales, caza y similares',
                    '621': 'Trabajadores en actividades pesqueras y de acuacultura',
                    '622': 'Trabajadores en actividades silvícolas y forestales',
                    '623': 'Trabajadores en actividades de caza, trampería y similares'
                }
            },
            '63': {
                'nombre': 'Operadores de maquinaria agropecuaria y forestal',
                'subgrupos': {
                    '631': 'Operadores de maquinaria agropecuaria y forestal'
                }
            },
            '69': {
                'nombre': 'Otros trabajadores en actividades agrícolas, ganaderas, forestales, caza y pesca, no clasificados anteriormente',
                'subgrupos': {
                    '699': 'Otros trabajadores en actividades agrícolas, ganaderas, forestales, caza y pesca, no clasificados anteriormente'
                }
            }
        }
    },
    '7': {
        'nombre': 'Trabajadores artesanales, en la construcción y otros oficios',
        'grupos': {
            '71': {
                'nombre': 'Trabajadores en la extracción y la edificación de construcciones',
                'subgrupos': {
                    '710': 'Supervisores de trabajadores en la extracción, albañiles y en acabados de la construcción',
                    '711': 'Trabajadores en la extracción',
                    '712': 'Albañiles y otros trabajadores en la edificación de construcciones',
                    '713': 'Yeseros, instaladores de pisos, climas, impermeabilizante, vidrio, etc., plomeros y pintores',
                    '719': 'Otros trabajadores relacionados con la extracción y la edificación de construcción, no clasificados anteriormente'
                }
            },
            '72': {
                'nombre': 'Artesanos y trabajadores en el tratamiento y elaboración de productos de metal',
                'subgrupos': {
                    '720': 'Supervisores de artesanos y trabajadores en el tratamiento y elaboración de productos de metal',
                    '721': 'Moldeadores, soldadores, hojalateros y pintores de metales',
                    '722': 'Herreros, cerrajeros, joyeros y artesanos en la elaboración de productos de metal',
                    '729': 'Otros trabajadores relacionados con el tratamiento y elaboración de productos de metal, no clasificados anteriormente'
                }
            },
            '73': {
                'nombre': 'Artesanos y trabajadores en la elaboración de productos de madera, papel, textiles y de cuero y piel',
                'subgrupos': {
                    '730': 'Supervisores de artesanos y trabajadores en la elaboración de productos de madera, papel, textiles y de cuero y piel',
                    '731': 'Artesanos y trabajadores en la elaboración de productos de madera',
                    '732': 'Artesanos y trabajadores en la elaboración de productos de papel, cartón y trabajos de impresión',
                    '733': 'Trabajadores en la preparación de fibras textiles y tejedores de fibras textiles',
                    '734': 'Artesanos en la elaboración de productos textiles, cuero, piel y similares',
                    '735': 'Tapiceros y trabajadores en el tratamiento y elaboración de productos de cuero y piel',
                    '739': 'Otros trabajadores relacionados con la elaboración de productos de madera, papel, textiles, cuero y piel, no clasificados anteriormente'
                }
            },
            '74': {
                'nombre': 'Artesanos y trabajadores en la elaboración de productos de hule, caucho, plásticos y de sustancias químicas',
                'subgrupos': {
                    '740': 'Supervisores de artesanos y trabajadores en la elaboración de productos de hule, caucho, plásticos y de sustancias químicas',
                    '741': 'Artesanos y trabajadores en la elaboración de productos de hule, caucho, plásticos y de sustancias químicas'
                }
            },
            '75': {
                'nombre': 'Trabajadores en la elaboración y procesamiento de alimentos, bebidas y productos de tabaco',
                'subgrupos': {
                    '750': 'Supervisores de trabajadores en la elaboración y procesamiento de alimentos, bebidas y productos de tabaco',
                    '751': 'Trabajadores en la elaboración y procesamiento de alimentos, bebidas y productos de tabaco',
                    '759': 'Otros trabajadores relacionados con la elaboración y procesamiento de alimentos, bebidas y productos de tabaco, no clasificados anteriormente'
                }
            },
            '76': {
                'nombre': 'Artesanos y trabajadores en la elaboración de productos de cerámica, vidrio, azulejo y similares',
                'subgrupos': {
                    '760': 'Supervisores de artesanos y trabajadores en la elaboración de productos de cerámica, vidrio, azulejo y similares',
                    '761': 'Artesanos y trabajadores en la elaboración de productos de cerámica, vidrio, azulejo y similares'
                }
            },
            '79': {
                'nombre': 'Otros trabajadores artesanales no clasificados anteriormente',
                'subgrupos': {
                    '799': 'Otros trabajadores artesanales no clasificados anteriormente'
                }
            }
        }
    },
    '8': {
        'nombre': 'Operadores de maquinaria industrial, ensambladores, choferes y conductores de transporte',
        'grupos': {
            '81': {
                'nombre': 'Operadores de instalaciones y maquinaria industrial',
                'subgrupos': {
                    '810': 'Supervisores de operadores de maquinaria industrial',
                    '811': 'Operadores de máquinas y equipos para la extracción en minas, canteras y pozos',
                    '812': 'Operadores de máquinas y equipos en la fabricación metalúrgica, fabricación de maquinaria y productos metálicos',
                    '813': 'Operadores de máquinas y equipos en la elaboración de productos químicos, plástico, tratamiento de agua y petroquímica',
                    '814': 'Operadores de máquinas para la madera y papel',
                    '815': 'Operadores de máquinas y equipos en la elaboración de productos textiles, cuero y piel',
                    '816': 'Operadores de máquinas en la elaboración de alimentos, bebidas y tabaco',
                    '817': 'Operadores de máquinas en la elaboración de cemento y productos de cerámica, vidrio y similares',
                    '818': 'Operadores de máquinas para la generación de energía',
                    '819': 'Otros operadores de instalaciones y maquinaria fija industrial, no clasificados anteriormente'
                }
            },
            '82': {
                'nombre': 'Ensambladores y montadores de herramientas, maquinaria, productos metálicos y electrónicos',
                'subgrupos': {
                    '820': 'Supervisores en procesos de ensamblado y montaje de maquinaria, herramientas y productos metálicos, eléctricos y electrónicos',
                    '821': 'Ensambladores y montadores de herramientas, maquinaria, productos metálicos y electrónicos'
                }
            },
            '83': {
                'nombre': 'Conductores de transporte y de maquinaria móvil',
                'subgrupos': {
                    '830': 'Supervisores de conductores de transporte y de maquinaria móvil',
                    '831': 'Conductores de transporte aéreo',
                    '832': 'Conductores de transporte marítimo',
                    '833': 'Conductores de transporte en vías férreas',
                    '834': 'Conductores de transporte terrestre con motor',
                    '835': 'Conductores de maquinaria móvil',
                    '899': 'Otros operadores de maquinaria industrial, ensambladores y conductores de transporte, no clasificados anteriormente'
                }
            },
            '89': {
                'nombre': 'Otros operadores de maquinaria industrial, ensambladores y conductores de transporte, no clasificados anteriormente',
                'subgrupos': {
                    '899': 'Otros operadores de maquinaria industrial, ensambladores y conductores de transporte, no clasificados anteriormente'
                }
            }
        }
    },
    '9': {
        'nombre': 'Trabajadores en actividades elementales y de apoyo',
        'grupos': {
            '91': {
                'nombre': 'Trabajadores de apoyo en actividades agropecuarias, forestales, pesca y caza',
                'subgrupos': {
                    '911': 'Trabajadores de apoyo en actividades agropecuarias',
                    '912': 'Trabajadores de apoyo en actividades forestales, pesca y caza'
                }
            },
            '92': {
                'nombre': 'Trabajadores de apoyo en la minería, construcción e industria',
                'subgrupos': {
                    '921': 'Trabajadores de apoyo en la minería y extracción',
                    '922': 'Trabajadores de apoyo en la construcción y la plomería',
                    '923': 'Trabajadores de apoyo en la industria'
                }
            },
            '93': {
                'nombre': 'Ayudantes de conductores de transporte, conductores de transporte de tracción humana y animal y cargadores',
                'subgrupos': {
                    '931': 'Ayudantes de conductores de transporte',
                    '932': 'Conductores de transporte en bicicleta y animal',
                    '933': 'Cargadores'
                }
            },
            '94': {
                'nombre': 'Ayudantes en la preparación de alimentos',
                'subgrupos': {
                    '941': 'Ayudantes en la preparación de alimentos'
                }
            },
            '95': {
                'nombre': 'Vendedores ambulantes',
                'subgrupos': {
                    '951': 'Vendedores ambulantes (excluyendo los de venta de alimentos)',
                    '952': 'Vendedores ambulantes de alimentos',
                    '959': 'Otros vendedores ambulantes no clasificados anteriormente'
                }
            },
            '96': {
                'nombre': 'Trabajadores domésticos, de limpieza, planchadores y otros trabajadores de limpieza',
                'subgrupos': {
                    '960': 'Supervisores en limpieza, amas de llaves, mayordomos y en estacionamientos',
                    '961': 'Trabajadores domésticos',
                    '962': 'Trabajadores de limpieza, recamaristas, mozos de limpieza y limpiadores de calzado',
                    '963': 'Lavadores y cuidadores de vehículos',
                    '964': 'Lavanderos y planchadores',
                    '965': 'Ayudantes de jardineros',
                    '966': 'Recolectores de desechos, material reciclable y de otros materiales'
                }
            },
            '97': {
                'nombre': 'Trabajadores de paquetería, de apoyo para espectáculos, mensajeros y repartidores de mercancías',
                'subgrupos': {
                    '971': 'Trabajadores de paquetería, empacado y de apoyo para espectáculos',
                    '972': 'Trabajadores repartidores de mensajería y mercancías (a pie o en bicicleta)',
                    '973': 'Lecturistas de medidores, recolectores de dinero y elevadoristas'
                }
            },
            '98': {
                'nombre': 'Otros trabajadores en actividades elementales y de apoyo, no clasificados anteriormente',
                'subgrupos': {
                    '989': 'Otros trabajadores en actividades elementales y de apoyo, no clasificados anteriormente'
                }
            },
            '99': {
                'nombre': 'Ocupaciones no especificadas',
                'subgrupos': {
                    '999': 'Ocupaciones no especificadas'
                }
            }
        }
    }
}


# Diccionario de Clasificación de Vacantes y Perfiles
# Estructura: 'Clave Mayor': {'nombre': 'Categoría', 'etiquetas': {'Clave Menor': {'nombre': 'Etiqueta', 'descripcion': '...'}}}

VACANTE_TAGS = {
    # 1. Clasificación por Sector o Industria
    '1': {
        'nombre': 'Por Sector o Industria',
        'etiquetas': {
            '11': {
                'nombre': 'Tecnología y TI',
                'descripcion': 'Empresas de software, desarrollo web, análisis de datos, ciberseguridad, telecomunicaciones.'
            },
            '12': {
                'nombre': 'Salud y Medicina',
                'descripcion': 'Hospitales, farmacéuticas, clínicas, investigación médica.'
            },
            '13': {
                'nombre': 'Finanzas y Banca',
                'descripcion': 'Bancos, seguros, inversión, contabilidad, análisis financiero.'
            },
            '14': {
                'nombre': 'Marketing y Publicidad',
                'descripcion': 'Agencias de publicidad, marketing digital, relaciones públicas, medios de comunicación.'
            },
            '15': {
                'nombre': 'Ingeniería y Manufactura',
                'descripcion': 'Producción, control de calidad, diseño industrial, automoción, construcción.'
            },
            '16': {
                'nombre': 'Comercio y Retail',
                'descripcion': 'Tiendas, comercio electrónico, ventas, gestión de inventario.'
            },
            '17': {
                'nombre': 'Educación',
                'descripcion': 'Escuelas, universidades, formación online, investigación académica.'
            },
            '18': {
                'nombre': 'Servicios al Cliente',
                'descripcion': 'Centros de llamadas, soporte técnico, atención al usuario.'
            },
            '19': {
                'nombre': 'Recursos Humanos',
                'descripcion': 'Reclutamiento, nóminas, capacitación, desarrollo organizacional.'
            },
            '110': {
                'nombre': 'Arte y Diseño',
                'descripcion': 'Diseño gráfico, ilustración, artes escénicas, moda, arquitectura.'
            },
            '111': {
                'nombre': 'Administración y Oficina',
                'descripcion': 'Asistente administrativo, secretaria, recepción, gestión de documentos.'
            }
        }
    },

    # 2. Clasificación por Función o Rol
    '2': {
        'nombre': 'Por Función o Rol',
        'etiquetas': {
            '21': {
                'nombre': 'Ventas y Desarrollo de Negocios',
                'descripcion': 'Ejecutivo de ventas, account manager, desarrollo de mercado.'
            },
            '22': {
                'nombre': 'Data y Análisis',
                'descripcion': 'Analista de datos, científico de datos, business intelligence.'
            },
            '23': {
                'nombre': 'Logística y Cadena de Suministro',
                'descripcion': 'Almacén, distribución, transporte, compras, importación/exportación.'
            },
            '24': {
                'nombre': 'Desarrollo de Software',
                'descripcion': 'Programación, arquitectura de software, QA (Garantía de Calidad).'
            },
            '25': {
                'nombre': 'Creatividad y Contenido',
                'descripcion': 'Redacción, diseño, fotografía, producción audiovisual.'
            },
            '26': {
                'nombre': 'Legal',
                'descripcion': 'Abogacía, derecho corporativo, cumplimiento (compliance).'
            }
        }
    },

    # 3. Clasificación por Intereses Personales (Soft Skills)
    '3': {
        'nombre': 'Por Intereses Personales (Soft Skills)',
        'etiquetas': {
            '31': {
                'nombre': 'Proactividad',
                'descripcion': 'Toma la iniciativa para realizar tareas o mejoras sin necesidad de esperar órdenes directas.'
            },
            '32': {
                'nombre': 'Responsabilidad',
                'descripcion': 'Cumple con sus obligaciones en tiempo y forma, asumiendo las consecuencias de sus actos.'
            },
            '33': {
                'nombre': 'Puntualidad',
                'descripcion': 'Respeta rigurosamente los horarios de entrada, reuniones y plazos de entrega establecidos.'
            },
            '34': {
                'nombre': 'Extroversión',
                'descripcion': 'Muestra energía y sociabilidad al interactuar con otras personas; se siente cómodo en entornos dinámicos.'
            },
            '35': {
                'nombre': 'Facilidad de palabra',
                'descripcion': 'Capacidad para expresar ideas verbalmente de manera fluida, clara y persuasiva.'
            },
            '36': {
                'nombre': 'Trabajo en equipo',
                'descripcion': 'Colabora activamente con compañeros, priorizando el objetivo grupal sobre el individual.'
            },
            '37': {
                'nombre': 'Orientación a resultados',
                'descripcion': 'Enfoca sus esfuerzos y energía en cumplir metas específicas y métricas de desempeño.'
            },
            '38': {
                'nombre': 'Tolerancia a frustración',
                'descripcion': 'Mantiene el control emocional y la productividad ante situaciones adversas, rechazos o fallos.'
            },
            '39': {
                'nombre': 'Adaptabilidad',
                'descripcion': 'Se ajusta rápidamente a cambios en el entorno, nuevas herramientas o diferentes métodos de trabajo.'
            },
            '310': {
                'nombre': 'Pensamiento crítico',
                'descripcion': 'Analiza la información y los hechos objetivamente antes de tomar una decisión o formar un juicio.'
            },
            '311': {
                'nombre': 'Empatía',
                'descripcion': 'Capacidad de comprender y validar las emociones y perspectivas de clientes o compañeros.'
            },
            '312': {
                'nombre': 'Atención al detalle',
                'descripcion': 'Realiza tareas con minuciosidad y precisión, detectando errores pequeños que otros pasan por alto.'
            },
            '313': {
                'nombre': 'Honestidad',
                'descripcion': 'Se conduce con rectitud, verdad y transparencia en el manejo de recursos e información.'
            },
            '314': {
                'nombre': 'Liderazgo',
                'descripcion': 'Habilidad para guiar, motivar e influir positivamente en un grupo para alcanzar un objetivo común.'
            },
            '315': {
                'nombre': 'Resolución de problemas',
                'descripcion': 'Identifica fallos rápidamente y propone soluciones lógicas y efectivas para arreglarlos.'
            },
            '316': {
                'nombre': 'Creatividad',
                'descripcion': 'Genera ideas originales, innovadoras o enfoques no convencionales para realizar una tarea.'
            },
            '317': {
                'nombre': 'Actitud de servicio',
                'descripcion': 'Muestra una disposición genuina y amable para ayudar y satisfacer las necesidades del cliente.'
            },
            '318': {
                'nombre': 'Negociación',
                'descripcion': 'Habilidad para dialogar y llegar a acuerdos beneficiosos entre partes con intereses diferentes.'
            },
            '319': {
                'nombre': 'Autonomía',
                'descripcion': 'Capacidad para trabajar de manera eficiente y productiva sin supervisión constante.'
            },
            '320': {
                'nombre': 'Organización',
                'descripcion': 'Estructura su trabajo, recursos y tiempo de manera ordenada para maximizar la eficiencia.'
            }
        }
    }
}


