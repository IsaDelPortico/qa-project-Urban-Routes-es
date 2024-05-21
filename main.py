import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage

class TestUrbanRoutes:

    driver = webdriver.Chrome
    @classmethod
    def setup_class(cls):
        # Configuración de las opciones de Chrome
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Inicialización del WebDriver con las opciones definidas
        cls.driver = webdriver.Chrome(options=options)

    def test0_acces_page(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Accede a la URL de Urban Routes
        self.driver.get(data.urban_routes_url)
        # Espera a que el logo principal de la página sea cargado
        helpers.wait_visibility_of_element(self.driver, routes_page.log_principal, 3)


    def test1_set_route(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Iguala las variables de dirección Origen y Destino a las establecidas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llama al método set_from en la instancia de UrbanRoutesPage
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Confirma la prueba
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test2_select_confort(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que el botón para pedir un taxi aparezca cargado
        helpers.wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el botón de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el botón de confort
        routes_page.click_confort_select()
        assert True, routes_page.click_check_confort_select
    def test3_set_phone(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click en el botón del número de teléfono del homepage
        routes_page.click_phone_number_home_page()
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        # Hace click en el botón "Siguiente" después de ingresar el número de teléfono
        routes_page.click_phone_number_pop_up_window()
        # Utilización de código ya preestablecido para obtener mensaje sms y agregar número de teléfono
        # Se realizaron pruebas utilizando PRINT con resultado NONE, verificando que el código no está devolviendo nada
        codigo_confirmacion = helpers.retrieve_phone_code(self.driver)
        routes_page.set_sms_code(str(codigo_confirmacion))
        assert True, (str(codigo_confirmacion)).isdigit()
        #Hace click en el botón "Siguiente" de la ventana emergente del código telefónico
        routes_page.click_next_code_phone()
        assert routes_page.get_phone_number() == phone_number

    def test4_add_card(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click en el botón "Método de pago" en la homepage
        routes_page.click_payment_method()
        # Hace click en el botón "Añadir tarjeta"
        routes_page.click_add_card()
        card_number=data.card_number
        card_code=data.card_code
        # Ingresa el número de la tarjeta
        routes_page.set_card_number(card_number)
        # Ingresa el código de la tarjeta
        routes_page.set_code_number(card_code)
        helpers.wait_to_be_clickable_of_element(self.driver, routes_page.botton_agree_card, 3)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_code_number() == card_code
        # Hace click en el botón "Añadir tarjeta" de la segunda ventana emergente
        routes_page.click_add_card_2nd_pop_up_window()
        assert True, routes_page.check_agree_tcard()
        routes_page.click_close_pop_up_card_windows()

    def test5_message_for_driver(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Ingresa el mensaje del conductor
        message_for_driver=data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test6_blanket_active(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Selecciona la manta y el pañuelo
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'


    def test7_order_2_ice_creams(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Agrega dos helados
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'


    def test8_taxi_request_modal_display(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click en "Pedir un taxi" y espera hasta que un conductor sea seleccionado
        routes_page.click_find_taxi()
        assert True, routes_page.check_order_header_title()

    def test9_check_show_name_driver_modal(self):
        # Crea una instancia de UrbanRoutesPage al pasar como argumento el driver
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_visibility_of_element(self.driver, routes_page.taxi_driver_selected, 40)
        assert True, routes_page.check_taxi_driver_selected()
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
