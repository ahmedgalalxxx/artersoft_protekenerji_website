# Protek Enerji E-Commerce Portal

A custom e-commerce portal module for Odoo 18, designed specifically for Protek Enerji customers.
Based on the official website: http://www.protekenerji.com/

## Website Analysis

### Brand Colors (from protekenerji.com)
| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Red | `#E3000F` | Links, buttons, accents |
| Primary Red Hover | `#EB0010` | Hover states |
| Dark Navy Blue | `#0A2251` | Header, footer background |
| Medium Blue | `#1443A3` | Footer sections |
| Light Blue | `#1853C9` | Newsletter section |
| Light Background | `#f1f8ff` | Section backgrounds |
| Dark Text | `#032e54` | Headings on light bg |
| Gray Text | `#777777` | Secondary text |

### Typography
- **Headings**: Raleway (Google Fonts)
- **Body**: Open Sans, Poppins (Google Fonts)

### Company Information
- **Company**: Protek Enerji Hiz. Tic. San. Ltd. Şti.
- **Phone**: 0850 441 58 60
- **Email**: info@protekenerji.com
- **Website**: https://www.protekenerji.com
- **Business**: Heat meters (Calorimeters), M-Bus converters, expense sharing systems

## Features

### Restricted Access
- **Login Required**: Users must be logged in to access the shop
- **Portal Only**: Customers can only access shopping functionality, not backend

### Pages Included
1. **Anasayfa (Home)** - Company introduction with icon boxes
2. **Shop** - Product catalog with categories and filters
3. **Cart** - Shopping cart management
4. **Checkout/Payment** - Secure checkout process
5. **Siparişlerim (My Orders)** - View current orders
6. **Geçmiş Siparişler (Past Orders)** - Order history
7. **Gizlilik Politikası (GDPR)** - Privacy policy page

### Design Features
- Exact brand colors from protekenerji.com
- Raleway & Open Sans fonts
- Responsive Bootstrap-based design
- Turkish language support
- Cookie consent for GDPR compliance
- Icon boxes matching original website

## Installation

1. Copy the `protekenerji` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the module from Apps menu

## Dependencies

- website_sale
- website_sale_stock
- portal
- auth_signup
- payment

## Configuration

After installation:
1. Configure your payment providers
2. Add products to the shop
3. Customize menu items as needed
4. Update contact information if needed

## Company Information

- **Company**: Protek Enerji Hiz. Tic. San. Ltd. Şti.
- **Website**: http://www.protekenerji.com/
- **Email**: info@protekenerji.com
- **Phone**: 0850 441 58 60
- **License**: LGPL-3

## Support

For support, please contact info@protekenerji.com


