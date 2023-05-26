import React, { InputHTMLAttributes, useState } from 'react';
import './styles.scss';

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label?: string;
  labelClassName?: string;
  ispassword?: boolean;
  placeholder?: string;
  className?: string;
};
export const Input = ({
  label,
  labelClassName,
  className,
  type = 'text',
  ispassword,
  onChange
}: InputProps) => {
  const [showPassword, setShowPassword] = useState(false);

  const togglePassword = () => {
    setShowPassword(!showPassword);
  };
  const passwordType = showPassword ? 'text' : 'password';

  return (
    <div className={`flex flex-col input-box ${className}`}>
      {label && (
        <label
          className={`tracking-widest uppercase text-2xs font-semibold mr-1 mb-1 text-green-400 ${labelClassName}`}>
          {label}
        </label>
      )}
      <div className='relative'>
        <input
          type={ispassword ? passwordType : type}
          onChange={onChange}
          className={`shadow-sm input-box-input`}
        />

        {ispassword && (
          <button
            type='button'
            onClick={togglePassword}
            className='absolute inset-y-0 right-0 flex items-center px-4 font-semibold text-xs  text-green-200'>
            <h6>{showPassword ? 'hide' : 'show'} </h6>
          </button>
        )}
      </div>
    </div>
  );
};

// export const TextArea = ({
//   label,
//   className,
//   normalLabel,
//   isWhiteLabel,
//   isPurple,
//   required,
//   labelClassName,
//   containerClass,
//   onChange,
//   ...props
// }) => {
//   return (
//     <div className={`flex flex-col ${containerClass}`}>
//       {label && (
//         <label
//           className={`${!normalLabel && 'tracking-tight uppercase'} font-semibold mr-1 mb-1  ${
//             isWhiteLabel ? 'text-white-100 text-base' : 'text-blue-100 text-xs'
//           }  ${labelClassName}`}>
//           {label} {required && <span className='text-pink-100 '>*</span>}
//         </label>
//       )}
//       <textarea
//         onChange={onChange}
//         className={`  rounded px-3 pt-2 ${
//           !isPurple ? 'bg-white-100 border' : 'bg-purple-30 border-none'
//         }  text-blue-100 text-sm  placeholder:text-sm md:text-base md:placeholder:text-base  font-medium placeholder-opacity-50 placeholder-purple-300 hover:border-blue-100 disabled:opacity-60 focus:border-blue-100  focus:outline-none resize-none ${className}`}
//         {...props}
//       />
//     </div>
//   );
// };
