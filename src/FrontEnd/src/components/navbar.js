import React from 'react';

export default function Navbar(props) {
    return (
        <div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="navbar-brand ms-3" style={{cursor: 'pointer'}}>MIA Proyecto 2</div>
                <div class="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul class="navbar-nav">
                        <li class="nav-item active">
                            <div class="nav-link" style={{cursor: 'pointer'}} onClick={() => props.setActiveOption("Consola")}>Consola</div>
                        </li>
                        <li class="nav-item">
                            <div class="nav-link" style={{cursor: 'pointer'}} onClick={() => props.setActiveOption("Login")}>Login</div>
                        </li>
                        <li class="nav-item">
                            <div class="nav-link" style={{cursor: 'pointer'}} onClick={() => props.setActiveOption("Reportes")}>Reportes</div>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    );
}