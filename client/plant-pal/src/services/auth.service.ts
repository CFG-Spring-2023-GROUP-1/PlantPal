import { toast } from 'react-toastify';
import { STORAGE_KEYS } from '../utils/constants';
import { apiService } from './base.service';

const LOGIN_URL = 'login';
const REGISTER_URL = '/register';


class AuthService {
  /** *********************************Login********************* */
  login = async (data: object) => {
    try {
      const response = await apiService.post(LOGIN_URL, data, false);
      // if (response.data) {
      //   const res = response.data;
      //   localStorage.setItem(STORAGE_KEYS.USER_ID, res.UserId);
      //   localStorage.setItem(STORAGE_KEYS.EMAIL, res.email);
      //   localStorage.setItem(STORAGE_KEYS.FIRST_NAME, res.first_name);
      //   localStorage.setItem(STORAGE_KEYS.LAST_NAME, res.last_name);
      //   return true;
      // }
      console.log(response)
    } catch (err: any) {
      // toast(err.response.status === 401 ? 'Incorrect Email Or Password' : err.message, {
      //   type: 'error'
      // });
    }
  };

  register = async (data: object) => {
    try {
      const response = await apiService.post(REGISTER_URL, data, false);
      if (response.data) {
        const res = response.data;
        localStorage.setItem(STORAGE_KEYS.USER_ID, res.UserId);
        localStorage.setItem(STORAGE_KEYS.EMAIL, res.email);
        localStorage.setItem(STORAGE_KEYS.FIRST_NAME, res.first_name);
        localStorage.setItem(STORAGE_KEYS.LAST_NAME, res.last_name);
        return true;
      }
    } catch (err: any) {
      toast(err.response.status === 401 ? 'Incorrect Email Or Password' : err.message, {
        type: 'error'
      });
    }
  };
}

export default new AuthService();
