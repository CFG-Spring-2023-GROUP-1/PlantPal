import React, { ButtonHTMLAttributes, ReactNode } from 'react';
import Loader from '../loader';

type ButtonColor = 'green';
type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  children: ReactNode;
  color: ButtonColor;
  className?: string;
  onClick?: () => void;
  loading?: boolean;
  disabled?: boolean;
};

const Button = ({ children, color, className, onClick, loading, disabled }: ButtonProps) => {
  return (
    <button
      onClick={onClick}
      className={`w-auto px-8 py-4 h-12 rounded-md ${
        color === 'green' ? 'bg-green-200 hover:bg-green-400' : ''
      } text-white transition-all text-xs tracking-[2px] ${
        loading || (disabled && 'bg-opacity-20')
      } ${className}`}
      disabled={loading || disabled}>
      {loading && <Loader size={10} />}
      {children}
    </button>
  );
};

export default Button;
