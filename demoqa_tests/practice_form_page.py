import os
from selene import browser, have, be, by

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_full_name(self, first_name, last_name):
        browser.element("#firstName").should(be.blank).type(first_name)
        browser.element("#lastName").should(be.blank).type(last_name)

    def fill_email(self, value):
        browser.element("#userEmail").should(be.blank).type(value)

    def fill_gender(self, value):
        browser.element(by.text(value)).click()

    def fill_user_number(self, value):
        browser.element("#userNumber").should(be.blank).type(value).press_tab()


    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirth').click().element(f'[value="{month - 1}"]').click()
        browser.element('#dateOfBirth').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month').element(by.text(f'{day}')).click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').click().type(subject).should(be.visible).press_enter()

    def fill_interest_sport(self):
        browser.element(by.text("Sports")).click()

    def fill_interest_music(self):
        browser.element(by.text("Reading")).click()

    def fill_interest_reading(self):
        browser.element(by.text("Music")).click()

    def fill_picture(self, value):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath(value))

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').should(be.blank).type(current_address)

    def fill_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).should(be.visible).press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).should(be.visible).press_enter()

    def submit_button(self):
        browser.element("#submit").click()

    def should_registered_user_with(self, full_name, email, gender, user_number, birthdate, subjects, hobby, file, address, location):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                birthdate,
                subjects,
                hobby,
                file,
                address,
                location,
            )
        )