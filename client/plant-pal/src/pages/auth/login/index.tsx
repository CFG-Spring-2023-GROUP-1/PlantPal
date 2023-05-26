/* eslint-disable react/no-unescaped-entities */
import React, { FormEvent, useState } from 'react';
import { Input } from '../../../components/base/input';
import LoginRegisterLayout from '../../../components/base/layout/login-register-layout';
const Login = () => {
  const emptyForm = {
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    keepSignedIn: false
  };

  const [formData, setFormData] = useState(emptyForm);
  const handleChange = (e: FormEvent<EventTarget>) => {
    const { name, value } = e.target as HTMLInputElement;
    setFormData({
      ...formData,
      [name]: value
    });
  };
  return (
    <LoginRegisterLayout type='login'>
      <div className='space-y-6'>
        <Input
          value={formData?.email}
          onChange={handleChange}
          label='email'
          className=''
          name={'username'}
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
