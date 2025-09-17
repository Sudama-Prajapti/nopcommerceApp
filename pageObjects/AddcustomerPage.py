import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Add customer Page
class AddCustomer:
    def __init__(self, driver):
        self.driver = driver

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"

    # Correct locator for roles dropdown
    txtcustomerRoles_xpath = "//select[@id='SelectedCustomerRoleIds']/option"
    lstitemAdministrators_xpath = "//li[@title='Administrators']"
    lstitemRegistered_xpath = "//li[@title='Registered']"
    lstitemGuests_xpath = "//select[@id='SelectedCustomerRoleIds']/option[normalize-space(text())='Guests']"
    lstitemVendors_xpath = "//li[@title='Vendors']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    textAdmin_Content_xpath = "//textarea[@id='AdminComment']"
    Btnsave_xpath = "//button[@name='save']"

    def clickOnCustomers_Menu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
        time.sleep(5)
    def clickonCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
        time.sleep(5)
    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setfirstname(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setlastname(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setCompanyname(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self, role):
        # Open the dropdown
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(2)

        if role == 'Registered':
            listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':   # <-- Correct name
            # remove Registered if already selected
            try:
                self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            except:
                pass
            listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Vendors':
            listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        # always safe to click using JS
        self.driver.execute_script("arguments[0].click();", listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setadminContent(self, content):
        self.driver.find_element(By.XPATH, self.textAdmin_Content_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.Btnsave_xpath).click()
