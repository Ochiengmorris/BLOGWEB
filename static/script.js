'use strict';

/**
 * navbar toggle in mobile
*/

const /** {NodeElement} */ $navbar = document.querySelector("[data-navbar]");
const /** {NodeElement} */ $navToggler = document.querySelector("[data-nav-toggler]");

$navToggler.addEventListener("click", () => $navbar.classList.toggle("active"));
$navToggler.addEventListener("click", () => $navToggler.classList.toggle("active"));
