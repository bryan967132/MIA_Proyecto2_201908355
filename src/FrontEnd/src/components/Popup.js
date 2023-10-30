import React from "react";
import './Popup.css'

export default function Popup({ isOpen, onClose, message }) {
    if (!isOpen) {
        return null;
    }

    return (
        <div className="popup">
            <div className="popup-content">
                <button onClick={onClose}>Cerrar</button>
                <div dangerouslySetInnerHTML={{ __html: message.replace(/\n/g, "<br/>") }} />
            </div>
        </div>
    );
};