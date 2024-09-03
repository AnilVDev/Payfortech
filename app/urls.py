from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name= 'app/login.html',authentication_form=LoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name= 'logout'),
    path('resend-otp/', views.OTPVerificationView.as_view(), name='resend_otp'),
    # path('password-change/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/password-change-done/'),name='passwordchange'),
    path('password-change/', views.password_change_view, name='passwordchange'),
    # path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='password_change_done'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('registration/verify-otp/', views.OTPVerificationView.as_view(), name='verify_otp'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-home', views.admin_home, name='admin_home'),
    path('registration_complete/', views.registration_complete, name='registration_complete'),
    path('max_attempts_exceeded/', views.max_attempts_exceeded, name='max_attempts_exceeded'),
    path('admin-home/user-list/', views.user_list, name='user_list'),
    path('user/delete/<int:user_id>/', views.DeleteUserView.as_view(), name='delete_user'),
    path('admin-home/products/', views.ProductListView.as_view(), name='product_list'),
    path('admin-home/add_product/', views.add_product, name='add_product'),
    path('admin-home/add_product_image/<int:product_id>/', views.add_product_images, name='add_product_image'),
    path('admin-home/edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('admin-home/categories/', views.category_list_and_add, name='category_list_and_add'),
    path('admin-home/categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('admin-home/edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('admin-home/brands/', views.brand_list_and_add, name='brand_list_and_add'),
    path('admin-home/brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('admin-home/edit_brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('admin-home/toggle_user_status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status')
         ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
