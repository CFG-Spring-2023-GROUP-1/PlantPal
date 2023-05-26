/* eslint-disable react/no-unescaped-entities */
import React, { ReactNode } from 'react';
import Img from '../../../assets/img/login.jpg';
import Logo from '../../../assets/Logo';
import Button from '../../../components/base/button';
import { ROUTE_KEYS } from '../../../utils/constants';
import { Link } from 'react-router-dom';

type FormType = 'login' | 'register';
const LoginRegisterLayout = ({ children, type }: { children: ReactNode; type: FormType }) => {
  return (
    <div className='flex max-h-[100vh] text-green-200'>
      <div
        className={`w-[50%] flex flex-col py-20 bg-brown-100 bg-opacity-75 space-y-10 px-10 sm:px-24`}>
        <Logo className='text-center' />
        <div className=' text-center w-full'>
          <h4 className=' text-lg sm:text-xl md:text-3xl'>
            {' '}
            {type == 'login' ? 'Welcome Back' : 'Get Started'}
          </h4>
          <p>Enter your details to get started</p>
        </div>

        {children}

        <Button color='green'> {type == 'register' ? 'Register' : 'Login'}</Button>

        <p className=' text-center mx-auto mt-6 text-green-500'>
          {type == 'login' ? "Don't have an account? " : 'Already have an account '}
          <span>
            <Link
              to={type == 'login' ? ROUTE_KEYS.REGISTER : ROUTE_KEYS.LOGIN}
              className=' font-semibold underline '>
              {type == 'login' ? 'Register' : 'Login'}
            </Link>
          </span>
        </p>
      </div>
      <img src={Img} alt='' className='w-[50%] max-h-[100vh]' />
    </div>
  );
};

export default LoginRegisterLayout;
