document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.querySelector(".search");
    const searchInput = document.querySelector(".search-location");
    const weatherImage = document.querySelector(".weather-image");
    const temperature = document.querySelector(".temperature h3");
    const condition = document.querySelector(".temperature p");
    const humidity = document.querySelector(".details p:nth-child(1)");
    const windSpeed = document.querySelector(".details p:nth-child(2)");
    const weatherCondition = document.querySelector(".details p:nth-child(3)");
    const hourlyForecast = document.querySelector(".hourly-forecast");
    const dayForecast = document.querySelector(".day-forecast");
    const sunrise = document.getElementById("sunrise");
    const sunset = document.getElementById("sunset");
    const pressure = document.getElementById("pressure");
    const airQuality = document.getElementById("air-quality");
    const umbrellaNeed = document.getElementById("umbrella-need");
    const uvIndex = document.getElementById("uv-index");
    const outdoors = document.getElementById("outdoors");
    const drivingSafety = document.getElementById("driving-safety");
    const clothing = document.getElementById("clothing");
    const heatStroke = document.getElementById("heat-stroke");

    const tempToggle = document.getElementById("temp-toggle");
    const modeToggle = document.getElementById("mode-toggle");

    let isCelsius = true;
    let currentWeatherData;
    let forecastData;

    searchButton.addEventListener("click", function() {
        const location = searchInput.value;
        if (location) {
            fetchWeather(location);
        }
    });
    tempToggle.addEventListener("click", function() {
        isCelsius = !isCelsius;
        updateCurrentWeather(currentWeatherData);
        updateForecast(forecastData);
        tempToggle.textContent = isCelsius ? "Switch to °F" : "Switch to °C";
    });


    function fetchWeather(location) {
        const apiKey = "ac05e5eb992ec6cdf33ecb2696537637"; // Replace with your actual API key
        const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;
        const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${location}&appid=${apiKey}&units=metric`;

        fetch(currentWeatherUrl)
            .then(response => response.json())
            .then(data => {
                currentWeatherData = data;
                updateCurrentWeather(data);
            });
            

        fetch(forecastUrl)
            .then(response => response.json())
            .then(data => {
                forecastData = data;
                updateForecast(data);
                updateHealthSafety(data);
            });
            
    }

    function updateCurrentWeather(data) {
        const weatherIcon = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
        weatherImage.src = weatherIcon;
        const temp = isCelsius ? `${data.main.temp}°C `: `${(data.main.temp * 9/5 + 32).toFixed(1)}°F`;
        temperature.textContent = temp;
        condition.textContent = data.weather[0].description;
        humidity.innerHTML =`<strong>Humidity:</strong> &#128167;${data.main.humidity}%`;
        windSpeed.innerHTML = `<strong>Wind Speed:</strong> &#x2634;${data.wind.speed} km/h`;
        weatherCondition.innerHTML = `<strong>Condition:</strong> ${data.weather[0].main}`;
        sunrise.textContent = new Date(data.sys.sunrise * 1000).toLocaleTimeString();
        sunset.textContent = new Date(data.sys.sunset * 1000).toLocaleTimeString();
        pressure.textContent = `${data.main.pressure} hPa`;
        airQuality.textContent = "Good"; // Placeholder, update with actual data if available
    }

    function updateForecast(data) {
        hourlyForecast.innerHTML = "";
        dayForecast.innerHTML = "";

        // Update hourly forecast
        for (let i = 0; i < 12; i++) { // Increased to 12 hours
            const forecast = data.list[i];
            const temp = isCelsius ? `${forecast.main.temp}°C` : `${(forecast.main.temp * 9/5 + 32).toFixed(1)}°F`;
            const hourElement = document.createElement("div");
            hourElement.classList.add("hour");
            hourElement.innerHTML = `
                ${new Date(forecast.dt * 1000).getHours()}<br>
                <img src="https://openweathermap.org/img/wn/${forecast.weather[0].icon}.png" alt="Weather Icon"><br>
                ${temp}
            `;
            hourlyForecast.appendChild(hourElement);
        }

        // Update daily forecast
        for (let i = 0; i < data.list.length; i += 8) {
            const forecast = data.list[i];
            const tempMax = isCelsius ? `${forecast.main.temp_max}°C` : `${(forecast.main.temp_max * 9/5 + 32).toFixed(1)}°F`;
            const tempMin = isCelsius ? `${forecast.main.temp_min}°C` : `${(forecast.main.temp_min * 9/5 + 32).toFixed(1)}°F`;
            const dayElement = document.createElement("div");
            dayElement.classList.add("day");
            dayElement.innerHTML = `
                <div class="day-name">${new Date(forecast.dt * 1000).toLocaleDateString('en-US', { weekday: 'long' })}</div>
                <div class="icon"><img src="https://openweathermap.org/img/wn/${forecast.weather[0].icon}.png" alt="Weather Icon"></div>
                <div class="temps">${tempMax} / ${tempMin}</div>
                <div class="precipitation">&#128167;${forecast.pop * 100}%</div>
            `;
            dayForecast.appendChild(dayElement);
        }
    } 
    function updateHealthSafety(data) {
        const forecast = data.list[0]; // Use the first forecasted weather data for current conditions

        // Update Umbrella Need
        if (forecast.weather[0].main.includes("Rain")) {
            umbrellaNeed.textContent = "Yes, it's going to rain.";
        } else {
            umbrellaNeed.textContent = "No, you don't need an umbrella.";
        }

        // Update UV Index
        const uv = forecast.main.temp > 30 ? "High" : "Low"; // Placeholder logic, replace with actual UV index data if available
        uvIndex.textContent = uv;

        // Update Outdoors Advice
        if (forecast.weather[0].main.includes("Clear")) {
            outdoors.textContent = "Great day for outdoor activities!";
        } else if (forecast.weather[0].main.includes("Rain")) {
            outdoors.textContent = "Better to stay indoors.";
        } else {
            outdoors.textContent = "Check the weather condition before going out.";
        }

        
    }        
    // Update Driving Safety
        if (forecast.weather[0].main.includes("Rain") || forecast.weather[0].main.includes("Snow")) {
            drivingSafety.textContent = "Drive carefully, road conditions might be hazardous.";
        } else {
            drivingSafety.textContent = "Safe to drive.";
        }

        // // Update Clothing Recommendation
        const temp = forecast.main.temp;
        if (temp < 10) {
            clothing.textContent = "Wear warm clothes.";
        } else if (temp < 20) {
            clothing.textContent = "Wear a light jacket.";
        } else {
            clothing.textContent = "Light clothing is fine.";
        }

        // // Update Heat Stroke Warning
        if (temp > 35) {
            heatStroke.textContent = "Warning: High risk of heat stroke.";
        } else {
            heatStroke.textContent = "Low risk of heat stroke.";
        }
    
});