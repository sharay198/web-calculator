from django.urls import reverse, resolve

# Create your tests here.



# class TestUrls:
# settings.configure()


def test_index_url():
    path = reverse('index')
    #print(resolve(path).view_name)
    assert resolve(path).view_name == 'index'

def test_exp_list_url():
    path = reverse('database')
    # print(resolve(path).view_name)
    assert resolve(path).view_name == 'database'
