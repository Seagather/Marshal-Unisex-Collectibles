<p id="top"></p>

# MARSHAL UNISEX COLLECTIBLES WEBSITE

[View live deployment of site here](http://marshal-unisex-collectibles.herokuapp.com/)

![responsive](readme-files/responsive.png)

Marshal Unisex Collectibles is an E-Commerce website for wrist watch brands. Majority of consumers now use online and digital channels to research prices or find product information. Whatever your interest, we tell your time in an extraordinary digital experience!
Moreso the site provides the necessary modern functionalities for the shop owner to manage vital content for products and services.

# Table of Contents

- [UX](#ux)
    - [Project Goals](#project-goals)
    - [UX Design](#ux-design)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Data Structure](#data-structure)
- [Database](#database)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

_<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>_

<a name="ux"/>

# UX

## Project Goals

The development of this project captures the essence of a full-stack site based around business logic used to control a centrally-owned dataset. The idea is to create an e-commerce site for wrist watch lovers using the Django framework with PostgreSQL database, then static file hosting with AWS, and a functional payment system using Stripe platform. 

## UX Design

The application was structured using bootstrap to maintain wide browser compatibility, consistency in design and extensibility to render responsive and modern website.

#### Typography

The following fonts from [Google Fonts](https://fonts.google.com/) were used for the site:

**Roboto Slab** was used for the logo, navigation and titles of the site.

**Exo** was used for the contents of the site.

**Georgia** was used for the call to action button.


#### Colors

The color scheme used in this project were meant to present the motifs as aesthetic pleasure to users.

-   ![#000](https://placehold.it/15/000/000000?text=+) `#000 - Black`

-   ![#343a40](https://placehold.it/15/343a40/000000?text=+) `#343a40 - Baltic Sea`

-   ![#fafafa](https://placehold.it/15/fafafa/000000?text=+) `#fafafa - Gray98`

-   ![#330000](https://placehold.it/15/330000/000000?text=+) `#330000 - Seal Brown`

-   ![#121315](https://placehold.it/15/121315/000000?text=+) `#121315 - Black Russian`

-   ![#D05F59](https://placehold.it/15/D05F95/000000?text=+) `#D05F59 - Moderate Red`

-   ![#dc3545](https://placehold.it/15/dc3545/000000?text=+) `#dc3545 - Amaranth`

-   ![#aab7c4](https://placehold.it/15/aab7c4/000000?text=+) `#aab7c4 - Heather`

-   ![#000080](https://placehold.it/15/000080/000000?text=+) `#000080 - Navy Blue`

-   ![##007bff](https://placehold.it/15/007bff/000000?text=+) `#007bff - Dodger Blue`

-   ![#17a2b8](https://placehold.it/15/17a2b8/000000?text=+) `#17a2b8 - Pelorous`

-   ![#00d9ff](https://placehold.it/15/00d9ff/000000?text=+) `#00d9ff - blue`

-   ![#6c757d](https://placehold.it/15/6c757d/000000?text=+) `#6c757d - Raven`

-   ![#28a745](https://placehold.it/15/28a745/000000?text=+) `#28a745 - Dark Lime Green`

-   ![#ffc107](https://placehold.it/15/ffc107/000000?text=+) `#ffc107 - Amber`

-   ![#17a2b8](https://placehold.it/15/17a2b8/000000?text=+) `#17a2b8 - Pelorous`


## User Stories

#### User Stories for Customers

| **As a shopper or site user I would like to**             | **So that I can**                                       |
| --------------------------------------------------------- | ------------------------------------------------------- |
| Navigate throughout the site with ease                    | Find product to purchase in an organised format         |
| View each product as a single unit                        | Ascertain detailed content of a particular brand        |
| View my current bag total                                 | Keep track of my spending limit                         |
| Search the site quickly                                   | Locate a particular product of interest                 |
| Create my own account                                     | Have my profile with the option to login and logout     |
| Create my personal profile                                | Save my information for future delivery and easy entry  |
| Sort products by category, name, price or rating          | Make an informed decision before transaction            |
| Be able to add/remove or edit products in my bag          | Regulate my orders and checkout                         |
| Be able to select the quantity and wrist size             | Avoid being overcharged and ensure perfect fitting      |
| Ensure secure transactions                                | Be convinced about my payment                           |
| Receive a post email confirmation about my order          | Be assured and have records of my transactions          |
| Read input by reviewers                                   | Be preinformed about product and services               |
| Review purchased product                                  | Let prospective users know how I feel about the product |
| Be able to reset or recover my password if needed         | Retain my personal account                              |
| Be able to contact the company                            | Channel enquiries or seek solution to issues            |


#### User Stories for Shop Administrators

| **As an administrator I would like to**                   | **So that I can**                                       |
| --------------------------------------------------------- | ------------------------------------------------------- |
| Manage Products and services                              | Maintain stock control system                           |
| Add/Edit/Update products and corresponding details        | Inform users about the latest product                   |
| Regulate prices                                           | Inform users about actionable prices                    |
| Delete products                                           | Remove sold out products and Update Database accordingly|
| Collate customer reviews                                  | Identify where to improve                               |


## Wireframes