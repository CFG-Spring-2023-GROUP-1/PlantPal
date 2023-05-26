/* eslint-disable react/no-unescaped-entities */
import React, { FormEvent, useState } from 'react';
import { Input } from '../../../components/base/input';
import LoginRegisterLayout from '../../../components/base/layout/login-register-layout';
const Register = () => {
  const emptyForm = {
    FirstName: '',
    LastName: '',
    Email: '',
    PhoneNo: '',
    Dob: '',
    Address: '',
    Password: '',
    ConfirmPassword: ''
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
    <LoginRegisterLayout type='register'>
      <div className='gap-5 gap-y-8 flex flex-wrap overflow-scroll no-scroll-bar'>
        <Input
          value={formData?.FirstName}
          onChange={handleChange}
          label='First name'
          className='w-[45%] '
          name={'FirstName'}
        />
        <Input
          value={formData?.LastName}
          onChange={handleChange}
          label='Last Name'
          className='w-[45%] '
          name={'LastName'}
        />
        <Input
          value={formData?.Email}
          onChange={handleChange}
          label='Email'
          className='w-[45%] '
          name={'Email'}
        />
        <Input
          value={formData?.Address}
          onChange={handleChange}
          label='Address'
          className='w-[45%] '
          name={'Address'}
        />
        <Input
          value={formData?.PhoneNo}
          onChange={handleChange}
          label='tel.'
          className='w-[45%] '
          name={'PhoneNo'}
        />
        <Input
          type='date'
          value={formData?.Dob}
          onChange={handleChange}
          label='Dob'
          className='w-[45%] '
          name={'Dob'}
        />
        <Input
          value={formData?.Password}
          onChange={handleChange}
          label='Password'
          className='w-[45%] '
          name={'password'}
          ispassword
        />
        <Input
          value={formData?.ConfirmPassword}
          onChange={handleChange}
          label='Confirm Password'
          className='w-[45%] '
          name={'ConfirmPassword'}
          ispassword
        />
      </div>
    </LoginRegisterLayout>
  );
};

export default Register;
