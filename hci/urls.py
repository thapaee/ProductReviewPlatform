"""hci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hci import views
import reviewer_company.views
urlpatterns = [
    path("admin/",admin.site.urls),
    path("",views.homepage,name="home"),
    path("services/",views.servicepage,name="services"),
    path("choose/",reviewer_company.views.choose,name="choose"),
    path("signup_choose/",reviewer_company.views.signup_landing,name="signup_landing"),
    path("signup_review/",reviewer_company.views.reviewer_signup,name="reviewer_signup"),
    path("signup_company/",reviewer_company.views.company_signup,name="company_signup"),
    path("choose/company",reviewer_company.views.company_login,name="company_login"),
    path("choose/reviewer",reviewer_company.views.company_login,name="reviewer_login"),
    path('t/',reviewer_company.views.cap,name='act'),
    path('review/',reviewer_company.views.review,name='ac'),
    path('/start/',views.start,name='start'),
    path('st/',views.store,name='store'),
    path('added/',reviewer_company.views.add_to_model,name='add_to_model'),
    path('company_dash/',reviewer_company.views.company_dash,name='company_dash'),
    path('company_profile/',reviewer_company.views.company_profile,name='company_profile'),
    path('reviewer_profile/',reviewer_company.views.reviewer_profile,name='reviewer_profile'),
    path('/add_product/',reviewer_company.views.add_product,name="upload"),
    path('/add_produc/',reviewer_company.views.add_final,name="uploadd"),
    path('view_product/',reviewer_company.views.view_product,name="view_products"),
    path('signedout/',views.signout,name="signout"),
    path('login_reviewer/',reviewer_company.views.reviewer_login,name="reviewer_login"),
    path('login_company/',reviewer_company.views.company_login,name="company_login"),
    path('record_review/',reviewer_company.views.record_expression,name="record_expression"),
    path('stats/',reviewer_company.views.company_visualize,name="company_visualize"),
    path('reports/',reviewer_company.views.company_reports,name="company_reports"),
    path('overview_reviewer/',reviewer_company.views.overview_reviewer,name="overview_reviewer"),
    path('overview_company/',reviewer_company.views.overview_company,name="overview_company"),
    path('thanks/',reviewer_company.views.questions_answer,name="reviewer_thanks"),
    path('incentives/',reviewer_company.views.incentives,name='incentives'),
    path('yu/',reviewer_company.views.sucess,name='s'),
    path('read_description/',reviewer_company.views.read_description,name='read_description'),
    path('sucess/',reviewer_company.views.product_added,name='added')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
