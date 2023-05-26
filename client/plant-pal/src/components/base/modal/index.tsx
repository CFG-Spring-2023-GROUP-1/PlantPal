import React, { FC, ReactNode } from 'react';
import { IoMdClose } from 'react-icons/io';
import Modal from 'react-modal';
import './styles.scss';

export type BaseModalProps = {
  show: boolean;
  title: string;
  coloredText: string;
  titleCta?: JSX.Element;
  hasBackButton?: boolean;
  description?: string;
  fixed?: boolean;
  wide?: boolean;
  onClose: () => void;
  onAfterOpen?: () => void;
  onBackButton?: () => void;
  titleIcon?: JSX.Element;
  titleIconColor?: 'danger' | 'info';
  footer?: JSX.Element;
  children?: ReactNode;
};

const BaseModal: FC<BaseModalProps> = ({
  show,
  onAfterOpen,
  onClose,
  title,
  fixed,
  children,
  coloredText,
  wide
}) => {
  const customStyles = {
    content: {
      top: '50%',
      left: '50%',
      right: 'auto',
      bottom: 'auto',
      marginRight: '-50%',
      transform: 'translate(-50%, -50%)',
      borderRadius: '10px',
      backgroundColor: '#fff',
      border: 'none',
      padding: '0px',
      overflow: 'unset'
    },
    overlay: {
      background: 'rgba(0, 0, 0, 0.4)',
      backdropFilter: 'blur(3px)',
      zIndex: 20000
    }
  };
  return (
    <Modal
      isOpen={show}
      onAfterOpen={onAfterOpen}
      onRequestClose={onClose}
      style={customStyles}
      contentLabel={title}
      shouldCloseOnOverlayClick={!fixed}
      ariaHideApp={false}>
      <div
        className={`p-14 bg-green-30 bg-opacity-70 relative rounded-md w-[85vw] max-h-[95vh] overflow-scroll no-scroll-bar ${
          wide ? 'mdLg:max-w-[1000px]' : 'max-w-[520px]'
        }`}>
        <IoMdClose
          className='text-[#374957] cursor-pointer absolute right-3 top-6 hover:text-black-100 transition-all'
          size={26}
          onClick={onClose}
        />
        <h4 className='pb-8 text-black'>
          {title} <span className='text-green-700'> {coloredText}</span>
        </h4>
        <div className=''>{children}</div>
      </div>
    </Modal>
  );
};

export default BaseModal;
