# Coin Watch
A project completed at EngHack 2018 at the University of Waterloo. This README is a duplicate of our [Devpost](https://devpost.com/software/coin-watch) submission.

## Inspiration

Cryptocurrencies are extremely popular, but 81% of initial coin offerings are fraudulent. We wanted to create an app that can help people avoid being coin-conned.

## What it does

Coin Watch analyzes websites of upcoming ICOs by looking at 7 key factors. We assign each ICO a credit score (between 0 and 1) based on abundance of social media links, presence and authenticity of developers, availability of GitHub repositories, roadmaps, and website terms and conditions/privacy policy. We also analyze text on the website and their whitepaper to look for language that alludes to false promise of returns.

## How I built it

The analysis is done with Python scripts that scrape the website looking for key elements. Sentiment analysis on the use of language is done with TextBlob. The web app is built with Flask.

## Challenges I ran into

We tried to use TensorFlow to perform image analysis on developers listed on the website but found that the quality was compromised. We also attempted to use an Indico API but was unable to access it.

## Accomplishments that I'm proud of
Learning to use Flask and Selenium, experimenting with TensorFlow.

## What I learned
Building web apps with Python with Flask, web scraping with Selenium

## What's next for Coin Watch
Improve our machine learning model.
