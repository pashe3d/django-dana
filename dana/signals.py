import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

import dana.tasks
from purchase.models import Payment
from bon.models import Person
import requests

from dana.settings import PASSWORD, USERNAME, SECRET
from purchase.models import Payment


# noinspection PyUnusedLocal
@receiver(post_save, sender=Payment)
def save_user_in_crm(sender, instance, **kwargs):
    try:
        send_to_crm(instance)
    except:
        print("Something else went wrong")


# noinspection PyUnusedLocal
@receiver(post_save, sender=Person)
def save_sub_user_in_crm(sender, instance, **kwargs):
    try:
        send_sub_user_to_crm(instance)
    except:
        print("Something else went wrong")


def send_to_crm(payment: Payment):
    if payment.type_id == Payment.Type.FREE:
        user = payment.order.user
        login_url = 'https://melkemun.danaabr.com/api/v1/Token/GetToken'
        login_data = {
            'Username': USERNAME,
            'Password': PASSWORD,
            'secret': SECRET,
        }
        login_response = requests.post(login_url, json=login_data)
        login_content = login_response.json()
        token = login_content['ResultData']['access_token']

        post_data = {
            'Subject': 'سرنخ: علاقه مند به خرید اشتراک',
            'FullName': user.name,
            'FullName_FirstName': '-',
            'FullName_LastName': user.name,
            'FullName_NamePrefix': '33203127-ABB1-420D-9F3E-628D6A896C92',
            'TemplateAttributeId': '4a8a117d-1d66-4d99-ae70-be809973188b',
            'ITStaffID': '11111111-1111-1111-1111-111111111111',
            'CompanyName': '',
            'JobTitle': '',
            'MobilePhone': user.phone,
            'Telephone': user.phone,
            'Email': '',
            'WebSiteUrl': '',
            'Address': '',
            'Address_ProvinceId': '11111111-1111-1111-1111-111111111111',
            'Address_CityId': '11111111-1111-1111-1111-111111111111',
            'Address_PostalCode': '',
            'Address_Street': '',
            'LeadSourceCode': 'A93D0B8B-33FE-49FF-8015-FCAD0C781565',
            'StatusCode': None,
            'CampaignId': None,
            'StateCode': None,
            'IndustryCode': None,
            'PersonnelCount': None,
            'ContactId': None,
            'OpportunityId': None,
            'AccountId': None,
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        response = requests.post('https://melkemun.danaabr.com/api/v1/CRM_Lead', json=post_data, headers=headers)
        content = response.json()

        row_id = content['ResultData']['rowId']

        requests.put(f'https://melkemun.danaabr.com/api/V1/CRM_Lead/ConvertLead/{row_id}', headers=headers)

    if payment.type_id == Payment.Type.ONLINE:
        user = payment.order.user
        login_url = 'https://melkemun.danaabr.com/api/v1/Token/GetToken'
        login_data = {
            'Username': USERNAME,
            'Password': PASSWORD,
            'secret': SECRET,
        }
        login_response = requests.post(login_url, json=login_data)
        login_content = login_response.json()
        token = login_content['ResultData']['access_token']

        post_data = {
            'FirstName': '-',
            'LastName': user.name,
            'FullName': user.name,
            'PersonalCode': '',
            'Email': '',
            'Tel': '',
            'TelExt': '',
            'MobilePhone': user.phone,
            'Address': '',
            'Description': '',
            'PositionId': '',
            'PS': '1234',
            'RepPS': '1234',
            'IPAddress': '',
            'ChangePasswordAtNextLogin': False,
            'CannotChangePassword': False,
            'PasswordNeverExpires': False,
            'DepartmentID': '22222222-2222-2222-2222-222222222222',
            'DomainId': '00000000-0000-0000-0000-000000000000',
            'UserType': 1,
            'UN': user.phone,
            'AvatarPath': '',
            'IsActiveDirectory': False,
            'IsLockedOut': False,
            'IsActive': False,
            'HasAccessToUserGroupRequests': False,
            'HasAccessToCompanyRequests': False,
            'HasAccessToDepartmentRequests': False,
            'HasAccessToItsDepartmentAndSubDepartments': False,
            'HasAccessToUserAssetDepartment': False,
            'HasAccessToUserAssetCompany': False,
            'EnableNotification': 7,
            'SendInvitationEmail': False,
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        response = requests.post('https://melkemun.danaabr.com/api/v1/users/add/user', json=post_data, headers=headers)

        content = response.json()

        row_id = content['ResultData']['rowId']
        factor_data = {
            'Title': 'فروش اشتراک',
            'AccountId': row_id,
            'iTStaffId': '11111111-1111-1111-1111-111111111111',
            'Status': '2190E6EC-D127-48B1-953E-70CC8812E986',
            'Purchaser': 'aaa',
            'TemplateAttributeId': 'E5C52760-FAF6-4691-B681-073A125FB0FE',
            'IsRemoved':'0'
        }

        requests.post(f'https://melkemun.danaabr.com/api/V1/WarehouseInvoice', json=factor_data, headers=headers)


def send_sub_user_to_crm(person: Person):
    if person.parent_id is not None:
        user = person
        login_url = 'https://melkemun.danaabr.com/api/v1/Token/GetToken'
        login_data = {'Username': USERNAME, 'Password': PASSWORD,
                      'secret': SECRET}
        login_response = requests.post(login_url, json=login_data)
        login_content = login_response.json()
        token = login_content['ResultData']['access_token']
        post_data = {
            "FirstName": "-",
            "LastName": user.name,
            "FullName": user.name,
            "PersonalCode": "",
            "Email": "",
            "Tel": "",
            "TelExt": "",
            "MobilePhone": user.phone,
            "Address": "",
            "Description": "",
            "PositionId": "",
            "PS": "1234",
            "RepPS": "1234",
            "IPAddress": "",
            "CheangePasswordAtNextLogin": False,
            "CannotChangePassword": False,
            "PasswordNeverExpires": False,
            "DepartmentID": "22222222-2222-2222-2222-222222222222",
            "DomainId": "00000000-0000-0000-0000-000000000000",
            "UserType": 1,
            "UN": user.phone,
            "AvatarPath": "",
            "IsActiveDirectory": False,
            "IsLockedOut": False,
            "IsActive": False,
            "HasAccessToUserGroupRequests": False,
            "HasAccessToCompanyRequests": False,
            "HasAccessToDepartmentRequests": False,
            "HasAccessToItsDepartmentAndSubDepartments": False,
            "HasAccessToUserAssetDepartment": False,
            "HasAccessToUserAssetCompany": False,
            "EnableNotification": 7,
            "SendInvitationEmail": False
        }
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + token}

        response = requests.post('https://melkemun.danaabr.com/api/v1/users/add/user', json=post_data, headers=headers)
        content = response.content
        content2 = content
