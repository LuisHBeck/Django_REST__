import requests


class TestCourse():
    headers = {
        'Authorization': 'Token 8822b738f4db5afa9fd75b11237cf0eab9457cec'
    }

    base_courses_url = 'http://127.0.0.1:8056/api/v2/courses/'


    def test_get_courses(self):
        response = requests.get(
            headers=self.headers,
            url=self.base_courses_url
        )
        assert response.status_code == 200


    def test_get_course(self):
        response = requests.get(
            headers=self.headers,
            url=f'{self.base_courses_url}3/'
        )
        assert response.status_code == 200


    def test_post_course(self):
        new_course = {
            'title': 'Vue.Js',
            'url': 'https://www.udemy.com/course/vuejs-2-the-complete-guidecz/ssss'
        }

        response = requests.post(
            headers=self.headers,
            url=self.base_courses_url,
            data=new_course
        )
        assert response.status_code == 201

    
    def test_put_course(self):
        update_coruse = {
            'title': 'Vue.Js - 3',
            'url': 'https://www.udemy.com/course/vuejs-2-the-complete-guide/test'
        }

        response = requests.put(
            headers=self.headers,
            url=f'{self.base_courses_url}3/',
            data=update_coruse
        )
        assert response.status_code == 200


    def test_delete_course(self):
        response = requests.delete(
            headers=self.headers,
            url=f'{self.base_courses_url}3/'
        )
        assert response.status_code == 204  