import pytest
from django.urls import reverse
from rest_framework import status
from api.models import Hero_content,Hero_features
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_admin_hero_content_list_test(api_client):
    Hero_content.objects.create(badge_text="badge text sample",main_heading="main heading sample",short_description="short description sample")
    url = reverse('admin_hero_content')
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['main_heading'] == "main heading sample"
    
    
@pytest.mark.django_db
def test_admin_hero_features(api_client):
    Hero_features.objects.create(feature="feature text sample")
    url = reverse('admin_hero_features')
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['feature'] == "feature text sample"
    
    
@pytest.mark.django_db
def test_admin_authenticated_hero_content_list(api_client):
    user = User.objects.create_user(username="admin", password="1234")
    api_client.force_authenticate(user=user)

    Hero_content.objects.create(
        badge_text="badge text sample",
        main_heading="main heading sample",
        short_description="short description sample"
    )

    url = reverse('admin_hero_content')
    response = api_client.get(url)

    assert response.status_code == 200