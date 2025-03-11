from demoqa_tests.practice_form_page import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_full_name('Sema', 'Semenov')
    registration_page.fill_email('sema@test.com')
    registration_page.fill_gender("Male")
    registration_page.fill_user_number("0123456789")
    registration_page.fill_date_of_birth(1995, 9, 13)
    registration_page.fill_subject('English')
    registration_page.fill_interest_sport()
    registration_page.fill_interest_music()
    registration_page.fill_interest_reading()
    registration_page.fill_picture("Proverka.jpg")
    registration_page.fill_current_address('text ' * 5)
    registration_page.fill_state_and_city('NCR', 'Delhi')
    registration_page.submit_button()
    registration_page.should_registered_user_with(
        "Sema Semenov",
        "sema@test.com",
        "Male",
        "0123456789",
        "13 September,1995",
        "English",
        "Sports, Music, Reading",
        "Proverka.jpg",
        'text text text text text',
        "NCR Delhi",
    )


