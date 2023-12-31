
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from borrower_registration_forms import (
    BorrowerScreen, BorrowerScreen1, BorrowerScreen2, BorrowerScreen3, BorrowerScreen4, BorrowerScreen5,
    BorrowerScreen6,BorrowerScreen7,BorrowerScreen8,BorrowerScreen9,BorrowerScreen10,BorrowerScreen11,
    BorrowerScreen12,BorrowerScreen13,BorrowerScreen14,BorrowerScreen15,BorrowerScreen16,BorrowerScreen17,
    BorrowerScreen18,BorrowerScreen19,Borrower
)
from borrower_dashboard import (DashboardScreen,user_helpers)
from lender_registration_form import (
    LenderScreen, LenderScreen1, LenderScreen2, LenderScreen3,
    LenderScreen_Edu_10th, LenderScreen_Edu_Intermediate,LenderScreen_Edu_Bachelors,
    LenderScreen_Edu_Masters, LenderScreen_Edu_PHD, LenderScreen4, LenderScreen5,
    LenderScreenInstitutionalForm1,LenderScreenInstitutionalForm2,LenderScreenInstitutionalForm3,
    LenderScreenInstitutionalForm4,LenderScreenInstitutionalForm5,LenderScreenIndividualForm1,
    LenderScreenIndividualForm2,LenderScreenIndividualForm3,LenderScreenIndividualBankForm1,
    LenderScreenIndividualBankForm2,LenderScreenInstitutionalBankForm1,LenderScreenInstitutionalBankForm2,
    KV
)
from lender_dashboard import (LenderDashboard, user_helpers1)
from dashboard import DashScreen
from new_loan_request import (NewloanScreen,NewScreen,user_helpers2)
#from users_module.test1 import LenderHomeScreen,KV
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.metrics import dp
from login import LoginScreen
from homepage import MainScreen
from signup import SignupScreen
#from  users_module.lender_home import LenderHome,lender_home
class MyApp(MDApp):
    def build(self):
        Builder.load_string(Borrower)
        Builder.load_string(KV)
        Builder.load_string(user_helpers)
        Builder.load_string(user_helpers1)
        Builder.load_string(user_helpers2)


        sm = ScreenManager(transition=SlideTransition())
        main_screen = MainScreen(name='MainScreen')
        login_screen = LoginScreen(name='LoginScreen')
        signup_screen = SignupScreen(name='SignupScreen')
        sm.add_widget(main_screen)
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)
        sm.add_widget(DashScreen(name='dashboard'))
        #sm.add_widget(LenderHome(name='LenderHome'))

        sm.add_widget(BorrowerScreen(name='borrower_registration_forms'))
        sm.add_widget(BorrowerScreen1(name='BorrowerScreen1'))
        sm.add_widget(BorrowerScreen2(name='BorrowerScreen2'))
        sm.add_widget(BorrowerScreen3(name='BorrowerScreen3'))
        sm.add_widget(BorrowerScreen4(name='BorrowerScreen4'))
        sm.add_widget(BorrowerScreen5(name='BorrowerScreen5'))
        sm.add_widget(BorrowerScreen6(name='BorrowerScreen6'))
        sm.add_widget(BorrowerScreen7(name='BorrowerScreen7'))
        sm.add_widget(BorrowerScreen8(name='BorrowerScreen8'))
        sm.add_widget(BorrowerScreen9(name='BorrowerScreen9'))
        sm.add_widget(BorrowerScreen10(name='BorrowerScreen10'))
        sm.add_widget(BorrowerScreen11(name='BorrowerScreen11'))
        sm.add_widget(BorrowerScreen12(name='BorrowerScreen12'))
        sm.add_widget(BorrowerScreen13(name='BorrowerScreen13'))
        sm.add_widget(BorrowerScreen14(name='BorrowerScreen14'))
        sm.add_widget(BorrowerScreen15(name='BorrowerScreen15'))
        sm.add_widget(BorrowerScreen16(name='BorrowerScreen16'))
        sm.add_widget(BorrowerScreen17(name='BorrowerScreen17'))
        sm.add_widget(BorrowerScreen18(name='BorrowerScreen18'))
        sm.add_widget(BorrowerScreen19(name='BorrowerScreen19'))
        sm.add_widget(LenderScreen(name='lender_registration_form'))
        sm.add_widget(LenderScreen1(name='LenderScreen1'))
        sm.add_widget(LenderScreen2(name='LenderScreen2'))
        sm.add_widget(LenderScreen3(name='LenderScreen3'))
        sm.add_widget(LenderScreen_Edu_10th(name='LenderScreen_Edu_10th'))
        sm.add_widget(LenderScreen_Edu_Intermediate(name='LenderScreen_Edu_Intermediate'))
        sm.add_widget(LenderScreen_Edu_Bachelors(name='LenderScreen_Edu_Bachelors'))
        sm.add_widget(LenderScreen_Edu_Masters(name='LenderScreen_Edu_Masters'))
        sm.add_widget(LenderScreen_Edu_PHD(name='LenderScreen_Edu_PHD'))
        sm.add_widget(LenderScreen4(name='LenderScreen4'))
        sm.add_widget(LenderScreen5(name='LenderScreen5'))
        sm.add_widget(LenderScreenInstitutionalForm1(name='LenderScreenInstitutionalForm1'))
        sm.add_widget(LenderScreenInstitutionalForm2(name='LenderScreenInstitutionalForm2'))
        sm.add_widget(LenderScreenInstitutionalForm3(name='LenderScreenInstitutionalForm3'))
        sm.add_widget(LenderScreenInstitutionalForm4(name='LenderScreenInstitutionalForm4'))
        sm.add_widget(LenderScreenInstitutionalForm5(name='LenderScreenInstitutionalForm5'))
        sm.add_widget(LenderScreenIndividualForm1(name='LenderScreenIndividualForm1'))
        sm.add_widget(LenderScreenIndividualForm2(name='LenderScreenIndividualForm2'))
        sm.add_widget(LenderScreenIndividualForm3(name='LenderScreenIndividualForm3'))
        sm.add_widget(LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1'))
        sm.add_widget(LenderScreenIndividualBankForm2(name='LenderScreenIndividualBankForm2'))
        sm.add_widget(LenderScreenInstitutionalBankForm1(name='LenderScreenInstitutionalBankForm1'))
        sm.add_widget(LenderScreenInstitutionalBankForm2(name='LenderScreenInstitutionalBankForm2'))

        sm.add_widget(DashboardScreen(name='borrower_dashboard'))
        sm.add_widget(LenderDashboard(name='lender_dashboard'))
        sm.add_widget(NewloanScreen(name='new_loan_request'))
        sm.add_widget(NewScreen(name='new'))
        # Set the initial screen to the login screen
        sm.current = 'MainScreen'

        # Set the screen manager for the login screen
        main_screen.app = self

        return sm





if __name__ == '__main__':
    MyApp().run()
