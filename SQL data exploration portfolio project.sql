
select * from covidvvaccinations 

-- select data that we are going to be use
select Location, date, total_cases, new_cases, total_deaths, population
from coviddeaths
order by 1,2

--Looking at total cases vs total deaths


select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Deathpercentage
from coviddeaths
where Location like '%states%'
order by 1,2



-- looking at total cases vs Population
-- Shows what percentage of population got covid


select Location, date, total_cases, Population, (total_cases/population)*100 as Percentinfected
from coviddeaths
order by 1,2



-- looking at countries with Highest infection rate comparted to population
select Location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentPopulationInfected
from coviddeaths
group by Location, population
order by PercentPopulationInfected desc



-- Showing countries with Highest Death Count per population
--casting totaldeaths data to int
select Location, MAX(cast(Total_deaths as signed)) as TotalDeathCount
from coviddeaths
where continent is not null
group by Location
order by totalDeathCount desc



-- showing the continent with highest death count
select Location, MAX(cast(Total_deaths as signed)) as TotalDeathCount
from coviddeaths
where continent is null
group by Location
order by totalDeathCount desc



-- population vs Vaccinations

-- Joining covid deaths and covid vaccinations datasets
select coviddeaths.continent, coviddeaths.location, coviddeaths.date, coviddeaths.population, covidvaccinations.new_vaccinations
from coviddeaths
join covidvaccinations on coviddeaths.location = covidvaccinations.location
and coviddeaths.date = covidvaccinations.date
where coviddeaths.continent is not null
order by 2,3


-- creating views of query data
create view TotalDeathCount as 
select Location, MAX(cast(Total_deaths as signed)) as TotalDeathCount
from coviddeaths
where continent is null
group by Location
order by totalDeathCount desc

