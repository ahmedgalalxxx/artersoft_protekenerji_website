/**
 * Protek Enerji - Custom JavaScript
 * E-Commerce Portal Frontend Scripts
 */

odoo.define('protekenerji.main', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');
    const ajax = require('web.ajax');

    /**
     * Protek Enerji Header Widget
     * Handles header scroll effects and mobile menu
     */
    publicWidget.registry.ProtekHeader = publicWidget.Widget.extend({
        selector: '.protek-enerji-portal',

        start: function () {
            this._super.apply(this, arguments);
            this._initScrollEffect();
            this._initSmoothScroll();
            this._initHomeRedirect();
            return Promise.resolve();
        },

        /**
         * Initialize Home menu redirect to main website
         */
        _initHomeRedirect: function () {
            // Find Home menu link and redirect to main website
            const homeLinks = document.querySelectorAll('header nav a[href="/"], header nav a[href="/?"]');
            homeLinks.forEach(function(link) {
                if (link.textContent.trim().toLowerCase() === 'home' || link.textContent.trim().toLowerCase() === 'anasayfa') {
                    link.setAttribute('href', 'http://www.protekenerji.com/');
                    link.setAttribute('target', '_self');
                }
            });
        },

        /**
         * Initialize header scroll effect
         */
        _initScrollEffect: function () {
            const header = document.querySelector('header');
            if (!header) return;

            let lastScroll = 0;

            window.addEventListener('scroll', () => {
                const currentScroll = window.pageYOffset;

                if (currentScroll > 100) {
                    header.classList.add('protek-header-scrolled');
                } else {
                    header.classList.remove('protek-header-scrolled');
                }

                lastScroll = currentScroll;
            });
        },

        /**
         * Initialize smooth scrolling for anchor links
         */
        _initSmoothScroll: function () {
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    const href = this.getAttribute('href');
                    if (href === '#') return;

                    e.preventDefault();
                    const target = document.querySelector(href);

                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        },
    });

    /**
     * Protek Product Card Widget
     * Handles product card hover effects and quick actions
     */
    publicWidget.registry.ProtekProductCard = publicWidget.Widget.extend({
        selector: '.protek-product-card',
        events: {
            'mouseenter': '_onMouseEnter',
            'mouseleave': '_onMouseLeave',
        },

        /**
         * Handle mouse enter on product card
         */
        _onMouseEnter: function () {
            this.$el.addClass('protek-card-hover');
        },

        /**
         * Handle mouse leave on product card
         */
        _onMouseLeave: function () {
            this.$el.removeClass('protek-card-hover');
        },
    });

    /**
     * Protek Cart Widget
     * Handles cart updates and notifications
     */
    publicWidget.registry.ProtekCart = publicWidget.Widget.extend({
        selector: '.protek-cart-page, .o_wsale_my_cart',
        events: {
            'click .js_add_cart_json': '_onUpdateCart',
            'change .js_quantity': '_onQuantityChange',
        },

        /**
         * Handle cart update via JSON
         */
        _onUpdateCart: function (ev) {
            this._showCartNotification('Cart updated successfully!');
        },

        /**
         * Handle quantity change
         */
        _onQuantityChange: function (ev) {
            // Debounce quantity changes
            clearTimeout(this._quantityTimeout);
            this._quantityTimeout = setTimeout(() => {
                this._showCartNotification('Quantity updated');
            }, 500);
        },

        /**
         * Show cart notification toast
         */
        _showCartNotification: function (message) {
            // Create toast notification
            const toast = document.createElement('div');
            toast.className = 'protek-toast position-fixed bottom-0 end-0 m-3 p-3 bg-dark text-white rounded shadow';
            toast.style.zIndex = '9999';
            toast.innerHTML = `
                <div class="d-flex align-items-center">
                    <i class="fa fa-check-circle text-success me-2"></i>
                    <span>${message}</span>
                </div>
            `;

            document.body.appendChild(toast);

            // Animate in
            setTimeout(() => {
                toast.style.opacity = '1';
                toast.style.transform = 'translateY(0)';
            }, 10);

            // Remove after delay
            setTimeout(() => {
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        },
    });

    /**
     * Protek Login Required Handler
     * Redirects to login when accessing restricted pages
     */
    publicWidget.registry.ProtekLoginRequired = publicWidget.Widget.extend({
        selector: '.protek-login-required',

        start: function () {
            this._super.apply(this, arguments);
            this._animateLockIcon();
            return Promise.resolve();
        },

        /**
         * Animate the lock icon
         */
        _animateLockIcon: function () {
            const lockIcon = this.$('.protek-lock-icon');
            if (lockIcon.length) {
                setInterval(() => {
                    lockIcon.addClass('animate');
                    setTimeout(() => lockIcon.removeClass('animate'), 500);
                }, 3000);
            }
        },
    });

    /**
     * Protek Order Tracking Widget
     * Handles order status updates and tracking
     */
    publicWidget.registry.ProtekOrderTracking = publicWidget.Widget.extend({
        selector: '.protek-orders-page, .protek-order-detail-page',

        start: function () {
            this._super.apply(this, arguments);
            this._initOrderHighlight();
            return Promise.resolve();
        },

        /**
         * Initialize order row highlighting
         */
        _initOrderHighlight: function () {
            const rows = this.$('.protek-order-row');
            rows.each(function (index) {
                $(this).css('animation-delay', `${index * 0.1}s`);
            });
        },
    });

    /**
     * Protek Form Validation Widget
     * Handles form validation and submission
     */
    publicWidget.registry.ProtekFormValidation = publicWidget.Widget.extend({
        selector: 'form.protek-address-form, form.protek-payment-form',
        events: {
            'submit': '_onFormSubmit',
            'blur input[required]': '_onInputBlur',
        },

        /**
         * Handle form submission
         */
        _onFormSubmit: function (ev) {
            const form = ev.currentTarget;
            if (!form.checkValidity()) {
                ev.preventDefault();
                ev.stopPropagation();
                this._showValidationErrors(form);
            }
            form.classList.add('was-validated');
        },

        /**
         * Handle input blur for real-time validation
         */
        _onInputBlur: function (ev) {
            const input = ev.currentTarget;
            if (!input.validity.valid) {
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
                input.classList.add('is-valid');
            }
        },

        /**
         * Show validation errors
         */
        _showValidationErrors: function (form) {
            const invalidInputs = form.querySelectorAll(':invalid');
            invalidInputs.forEach(input => {
                input.classList.add('is-invalid');
            });

            // Scroll to first invalid input
            if (invalidInputs.length > 0) {
                invalidInputs[0].scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
                invalidInputs[0].focus();
            }
        },
    });

    /**
     * Protek GDPR Cookie Consent
     * Handles cookie consent for GDPR compliance
     */
    publicWidget.registry.ProtekCookieConsent = publicWidget.Widget.extend({
        selector: 'body',

        start: function () {
            this._super.apply(this, arguments);
            this._checkCookieConsent();
            return Promise.resolve();
        },

        /**
         * Check if cookie consent is needed
         */
        _checkCookieConsent: function () {
            const consent = localStorage.getItem('protek_cookie_consent');
            if (!consent) {
                this._showCookieBar();
            }
        },

        /**
         * Show cookie consent bar
         */
        _showCookieBar: function () {
            const bar = document.createElement('div');
            bar.className = 'protek-cookie-bar position-fixed bottom-0 start-0 end-0 bg-dark text-white p-3';
            bar.style.zIndex = '9999';
            bar.innerHTML = `
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-md-8">
                            <p class="mb-md-0 mb-2">
                                <i class="fa fa-cookie-bite me-2"></i>
                                We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.
                                <a href="/protek/gdpr" class="text-danger">Learn more</a>
                            </p>
                        </div>
                        <div class="col-md-4 text-md-end">
                            <button class="btn btn-danger btn-sm me-2 protek-accept-cookies">Accept</button>
                            <button class="btn btn-outline-light btn-sm protek-decline-cookies">Decline</button>
                        </div>
                    </div>
                </div>
            `;

            document.body.appendChild(bar);

            // Handle accept
            bar.querySelector('.protek-accept-cookies').addEventListener('click', () => {
                localStorage.setItem('protek_cookie_consent', 'accepted');
                bar.remove();
            });

            // Handle decline
            bar.querySelector('.protek-decline-cookies').addEventListener('click', () => {
                localStorage.setItem('protek_cookie_consent', 'declined');
                bar.remove();
            });
        },
    });

    return {
        ProtekHeader: publicWidget.registry.ProtekHeader,
        ProtekProductCard: publicWidget.registry.ProtekProductCard,
        ProtekCart: publicWidget.registry.ProtekCart,
        ProtekLoginRequired: publicWidget.registry.ProtekLoginRequired,
        ProtekOrderTracking: publicWidget.registry.ProtekOrderTracking,
        ProtekFormValidation: publicWidget.registry.ProtekFormValidation,
        ProtekCookieConsent: publicWidget.registry.ProtekCookieConsent,
    };
});

