/* eslint-disable react/no-unescaped-entities */
import React, { FormEvent, useState } from 'react';
import { Input } from '../../../components/base/input';
import LoginRegisterLayout from '../../../components/base/layout/login-register-layout';
import authService from '../../../services/auth.service';
const Login = () => {
  const emptyForm = {
    email: '',
    password: ''
  };

  const [formData, setFormData] = useState(emptyForm);
  const [loading, setLoading] = useState(false);
  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const login = async () => {
    setLoading(true);
    const res = await authService.login(formData);
    console.log(res);
    setLoading(false);
  };
  return (
    <LoginRegisterLayout type='login' onLogin={login} loading={loading}>
      <div className='space-y-6'>
        <Input
          value={formData?.email}
          onChange={handleChange}
          label='email'
          className=''
          name={'email'}
        />
        <Input
          value={formData?.password}
          onChange={handleChange}
          label='Password'
          className=''
          name={'password'}
          ispassword
        />
      </div>
    </LoginRegisterLayout>
  );
};

export default Login;
