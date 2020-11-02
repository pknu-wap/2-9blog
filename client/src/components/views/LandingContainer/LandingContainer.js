import React from 'react';
import './LandingContainer.scss';
import laptop from './laptop.jpg';
import arrow from './arrow.png';
import { NavLink } from "react-router-dom";

function LandingContainer() {
    return (
        <div id="landing-container">
            <img src={laptop} />
            <div className="img-outer"></div>
            <div className="text-inner">
                <p className="study-text">하루동안 공부한 것을</p>
                <p className="write-text">기록해 보세요.</p>
            </div>
                <NavLink exact to="/write" className="go-write">기록하러 가기<hr></hr>
                    <img src={arrow} />
                </NavLink>
        </div>
    )
}

export default LandingContainer