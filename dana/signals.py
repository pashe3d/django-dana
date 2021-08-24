from django.db.models.signals import post_save
from django.dispatch import receiver

from purchase.models import Payment


# noinspection PyUnusedLocal
@receiver(post_save, sender=Payment)
def save_user_in_crm(sender, instance, **kwargs):
    user = instance.order.user

    post_data = {
        'FirstName': '',
        'LastName': '',
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
        'CheangePasswordAtNextLogin': False,
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
        'SendInvitationEmail': False
    }
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer UTnHbSSqQDR-OA3dgvsacC_1hXSu0J9dLDh0fZJc3QD25q3Wlr6JT-1-gcCXxuNspPF9bMsfPnUUZCuDNbQI0PQpRfl8vBs33cbOD8mOd7MqcsW7fadJUTEL3L3gHM50mIy0Y1Pc9hh8jm5zQoTPzim8azO61UW7kaZVxCUqpOTSJ51O4NMQ-59irxsKDNCe6VNcj1p-fJ5toKPZA7o7aY_eW1kZ03t8Z6sz-QMCNkHaIMXCu1wHI7vDNob95gMMOchgvgOiefQ5SRNMvx9El1g3fPiu87d9DQ6wX77_7Zx2pMfenhC7zsasJYlcSqv7LDmQJhnpEnUh8qEjZuGYEy9WVqQuULTFZSvnJkEtPg8lZVgDOYhTpTufODwp_Xq2D8F3mOj9vli0oTI3gYLG6h6MhW7b1YXoziyqfmIVYzWPgWjqm-Oss8_uUJRu2kd0yPHtIa4cQKHw4aakfj87ZJvAd3KTRCN2esyXoXUB0PSQqdiTPzJ4DLBirljvx-wQ0ghTDp-ZfBoEx2G5GS3Ss2ZAbavj2v9WQ6Ykey5YNI_Y8yVsTVIY2s19r6oVUmz2zMmmKyY1ziIUUU2OX0PukGFLPSH7Fnk6tSjFHm06_QRn_bxMVfUSoP-x3BaygGDvH16rdOj-Hhxi6_BuBABeTAgx-GiQuxPu10MoEqH18oSwvUwGIxWILRhUM2Idtao59D86icHPnaol_kPwRGS3KGuwkhI'}

    response = requests.post('https://melkemun.danaabr.com/api/v1/users/add/user', data=post_data, headers=headers)
    content = response.content
