import os
from selene import browser, have, be, by

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_full_name(self, value):
        browser.element("#firstName").should(be.blank).type(value)
        browser.element("#lastName").should(be.blank).type(value)

    def fill_email(self, value):
        browser.element("#userEmail").should(be.blank).type(value)

    def fill_gender(self, value):
        browser.element(by.text(value)).click()

    def fill_user_number(self, value):
        browser.element("#userNumber").should(be.blank).type(value).press_tab()


    def fill_date_of_birth(self, value):
        browser.element("#dateOfBirthInput").type(value).press_enter()

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_tab()

    def fill_interest_sport(self):
        browser.element(by.text("Sports")).click()

    def fill_interest_music(self):
        browser.element(by.text("Reading")).click()

    def fill_interest_reading(self):
        browser.element(by.text("Music")).click()

    def fill_picture(self, value):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath(value))

    def fill_full_address(self, value):
        browser.element("#currentAddress").type(value)
        browser.element("#state").click().element(by.text("NCR")).click()
        browser.element("#city").click().element(by.text("Delhi")).click()

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






