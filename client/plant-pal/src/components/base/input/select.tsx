import React from 'react';
import ReactSelect from 'react-select';
import './styles.scss';

export type MultiSelectType = {
  label: string;
  value: string;
};
type SelectProps = {
  selectedOption: MultiSelectType;
  options: MultiSelectType[];
  onChange: () => void;
  placeholder?: string;
  className?: string;
  isMulti?: boolean;
  label: string;
};
const Select = ({
  selectedOption,
  options,
  onChange,
  placeholder,
  className,
  isMulti,
  label,
  ...rest
}: SelectProps) => {
  return (
    <div className={`${className} flex flex-col sm:flex-col gap-1`}>
      {label && (
        <label className='text-blue-100 font-semibold text-xs tracking-tight uppercase mr-1 mb-1'>
          {label}
        </label>
      )}
      <ReactSelect
        defaultValue={selectedOption}
        onChange={onChange}
        options={options}
        {...rest}
        placeholder={placeholder}
        isMulti={isMulti}
        className='select-input'
      />
    </div>
  );
};

export default Select;
