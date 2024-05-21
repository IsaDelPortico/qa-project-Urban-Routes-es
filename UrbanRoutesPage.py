from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    log_principal = (By.CLASS_NAME, 'logo-image')
    botton_round = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    confort_select = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')
    botton_phone_num = (By.CLASS_NAME, 'np-text')
    input_phone = (By.ID, 'phone')
    botton_phone_num_pop_up_window = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button')
    botton_next_phone_code = (By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')
    sms_code_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    botton_payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    botton_add_card = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_number_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    botton_agree_card=(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)')
    check_agree_card= (By.CSS_SELECTOR,'#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3)')
    message_for_driver_field=(By.ID, 'comment')
    blanket_selector=(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span')
    blanket_value=(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
    blanket_label = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div')
    ice_cream_plus=(By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    botton_find_taxi = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    taxi_driver_selected = (By.XPATH,'/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/img')
    ice_cream_count = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
    order_header_title = (By.CLASS_NAME, 'order-header-title')
    close_pop_up_card_windows=(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        # Encuentra y envía los datos en el campo "dirección de origen"
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        # Encuentra y envía los datos en el campo "dirección de destino"
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_botton_round (self):
        # Hace click en el botón "Pedir un taxi" en el homepage
        self.driver.find_element(*self.botton_round).click()

    def click_confort_select (self):
        # Hace click en el botón "Confort" del homepage
        self.driver.find_element(*self.confort_select).click()

    def click_check_confort_select (self):
        # Comprueba que el botón "Confort" haya sido seleccionado
        elemento = self.driver.find_element(*self.blanket_label)
        confort_is_check= elemento.is_displayed()
        return confort_is_check

    def click_phone_number_home_page (self):
        # Hace click en el botón del homepage para ingresar número de teléfono
        self.driver.find_element(*self.botton_phone_num).click()

    def set_phone_number(self, number_phone):
        # Encuentra y envía los datos en el campo número de teléfono
        self.driver.find_element(*self.input_phone).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.botton_phone_num).get_property('outerText')
    def click_phone_number_pop_up_window(self):
        # Hace click en el botón para agregar el número de teléfono desde la ventana emergente
        self.driver.find_element(*self.botton_phone_num_pop_up_window).click()

    def set_sms_code(self, code_sms):
        # Encuentra y envía los datos del código sms en el campo correspondiente
        self.driver.find_element(*self.sms_code_field).send_keys(code_sms)

    def click_next_code_phone(self):
       # Hace click para cerrar la ventana emergente del número de teléfono
       self.driver.find_element(*self.botton_next_phone_code).click()

    def check_send_phone_code(self):
        # Comprueba que el botón "Confort" ha sido seleccionado
        elemento = self.driver.find_element(*self.pop_up_window_phone_code)
        send_phone_code_is_check = elemento.is_displayed()
        return send_phone_code_is_check
    def click_payment_method(self):
        # Hace click en el botón "Método de pago" del homepage
        self.driver.find_element(*self.botton_payment_method).click()

    def click_add_card(self):
        # Hace click en el botón "Añadir una tarjeta"
        self.driver.find_element(*self.botton_add_card).click()

    def set_card_number(self, number_card):
        # Encuentra y envía los datos en el campo del número de tarjeta
        self.driver.find_element(*self.card_number_field).send_keys(number_card)

    def set_code_number(self, code_card):
        # Encuentra el campo del código de la tarjeta y envía el código
        code_field = self.driver.find_element(*self.card_code_number_field)
        code_field.send_keys(code_card)
        # Simula presionar la tecla TAB para hacer cambio de enfoque
        code_field.send_keys(Keys.TAB)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_code_number(self):
        return self.driver.find_element(*self.card_code_number_field).get_property('value')

    def click_add_card_2nd_pop_up_window(self):
        # Hace click en el botón "Añadir una tarjeta" en la segunda ventana emergente
        self.driver.find_element(*self.botton_agree_card).click()

    def check_agree_tcard(self):
        # Comprueba que el boton "Confort" ha sido seleccionado
        elemento = self.driver.find_element(*self.check_agree_card)
        agree_tcard = elemento.is_displayed()
        return agree_tcard

    def click_close_pop_up_card_windows(self):
       # Hace click para cerrar la ventana emergente del número de teléfono
       self.driver.find_element(*self.close_pop_up_card_windows).click()


    def set_message_for_driver(self, driver_message):
        # Encuentra y envía los datos en el campo de mensaje para el conductor
        self.driver.find_element(*self.message_for_driver_field).send_keys(driver_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def click_blanket_selector(self):
        # Hace click para seleccionar manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()

    def get_blanket_value(self):
        return self.driver.find_element(*self.blanket_value).get_property('value')

    def click_ice_cream_plus(self):
        # Hace click para agregar helados
        self.driver.find_element(*self.ice_cream_plus).click()

    def get_ice_cream_value(self):
        return self.driver.find_element(*self.ice_cream_count).get_property('outerText')

    def click_find_taxi(self):
        # Hace click para pedir un taxi
        self.driver.find_element(*self.botton_find_taxi).click()

    def check_botton_find_taxi(self):
        # Comprueba que el botón "Buscar taxi" aparezca
        elemento = self.driver.find_element(*self.botton_find_taxi)
        botton_find_taxi = elemento.is_displayed()
        return botton_find_taxi


    def check_taxi_driver_selected(self):
        # Comprueba que el botón "Confort" ha sido seleccionado
        elemento = self.driver.find_element(*self.taxi_driver_selected)
        taxi_driver_selected = elemento.is_displayed()
        return taxi_driver_selected

    def check_order_header_title(self):
        # Comprueba que el botón "Confort" ha sido seleccionado
        elemento = self.driver.find_element(*self.order_header_title)
        order_header_title_show = elemento.is_displayed()
        return order_header_title_show