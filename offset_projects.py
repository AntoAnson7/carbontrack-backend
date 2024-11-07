import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carbontrack.settings")
django.setup()

from api.models import CarbonOffsetProject

carbon_offset_projects = [
   {
       "name": "Eden Reforestation Project",
       "description": "Eden Reforestation Projects plants native trees in areas affected by deforestation, helping to restore ecosystems, combat climate change, and reduce poverty by employing local villagers.",
       "location": "Madagascar, Kenya, Haiti",
       "offset_potential_tons": 0.1,
       "category": "Reforestation",
       "benefits": ["Provides local employment", "Restores biodiversity", "Sequesters CO2"],
       "activities": ["Tree planting", "Community engagement", "Ecosystem restoration"],
       "link": "https://www.edenprojects.org/",
       "image_url": "https://www.edenprojects.org/uploads/1/2/1/8/121898596/trees-planted_orig.jpg"
   },
   {
       "name": "Cool Earth Rainforest Protection",
       "description": "Cool Earth collaborates with rainforest communities to prevent deforestation, preserving biodiversity and storing CO2.",
       "location": "Amazon rainforest, Papua New Guinea",
       "offset_potential_tons": 0.2,
       "category": "Forest Conservation",
       "benefits": ["Protects biodiversity", "Supports local communities", "Prevents deforestation"],
       "activities": ["Monitoring forests", "Sustainable income generation", "Community-led initiatives"],
       "link": "https://www.coolearth.org/",
       "image_url": "https://www.coolearth.org/wp-content/uploads/2020/05/CE-Homepage-Header.jpg"
   },
   {
       "name": "Makara Wind Power Project",
       "description": "The Makara Wind Power Project generates renewable energy, reducing reliance on fossil fuels and lowering carbon emissions.",
       "location": "Sri Lanka",
       "offset_potential_tons": 0.3,
       "category": "Renewable Energy - Wind",
       "benefits": ["Reduces greenhouse gases", "Promotes clean energy", "Creates local jobs"],
       "activities": ["Wind turbine construction", "Energy production", "Community education"],
       "link": "https://www.goldstandard.org/projects/makara-wind-power",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_MakaraWind.jpg"
   },
   {
       "name": "Bangladesh Solar Home Systems",
       "description": "Provides solar energy to rural households in Bangladesh, reducing CO2 emissions from fossil fuels.",
       "location": "Bangladesh",
       "offset_potential_tons": 0.25,
       "category": "Renewable Energy - Solar",
       "benefits": ["Improves air quality", "Reduces fossil fuel use", "Enhances living standards"],
       "activities": ["Solar panel installation", "Maintenance training", "System upkeep"],
       "link": "https://carbonfund.org/project/bangladesh-solar-home-systems/",
       "image_url": "https://carbonfund.org/wp-content/uploads/2020/05/Solar-Home-Systems.jpg"
   },
   {
       "name": "Rwanda Clean Cookstoves",
       "description": "This project distributes efficient cookstoves, reducing CO2 emissions from traditional wood-burning stoves.",
       "location": "Rwanda",
       "offset_potential_tons": 0.15,
       "category": "Clean Cooking",
       "benefits": ["Improves health", "Reduces deforestation", "Increases fuel efficiency"],
       "activities": ["Manufacturing cookstoves", "User education", "Sustainable cooking technology"],
       "link": "https://www.goldstandard.org/projects/rwanda-clean-cookstoves",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_RwandaCookstove.jpg"
   },
   {
       "name": "Uganda Domestic Biogas Program",
       "description": "Helps households in Uganda produce biogas from organic waste, reducing reliance on firewood for cooking.",
       "location": "Uganda",
       "offset_potential_tons": 0.18,
       "category": "Biogas",
       "benefits": ["Reduces firewood use", "Improves sanitation", "Lowers household emissions"],
       "activities": ["Biogas digester installation", "Training on maintenance", "Waste recycling"],
       "link": "https://www.goldstandard.org/projects/uganda-domestic-biogas",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_UgandaBiogas.jpg"
   },
   {
       "name": "Solar Water Heaters in South Africa",
       "description": "This project installs solar water heaters, reducing CO2 emissions from water heating using fossil fuels.",
       "location": "South Africa",
       "offset_potential_tons": 0.1,
       "category": "Renewable Energy - Solar",
       "benefits": ["Reduces energy costs", "Provides clean energy", "Decreases carbon emissions"],
       "activities": ["Heater installation", "User education", "Maintenance training"],
       "link": "https://carbonfund.org/project/solar-water-heaters-south-africa/",
       "image_url": "https://carbonfund.org/wp-content/uploads/2019/07/solar-water-heaters.jpg"
   },
   {
       "name": "Brazilian Amazon Forest Protection",
       "description": "This project protects sections of the Amazon rainforest, preserving habitats and preventing CO2 emissions.",
       "location": "Brazil",
       "offset_potential_tons": 0.5,
       "category": "Forest Conservation",
       "benefits": ["Preserves biodiversity", "Reduces CO2 release", "Protects indigenous lands"],
       "activities": ["Forest monitoring", "Supporting native rights", "Biodiversity conservation"],
       "link": "https://www.conservation.org/projects/protecting-the-amazon",
       "image_url": "https://www.conservation.org/images/default-source/default-album/amazon.jpg"
   },
   {
       "name": "Indian Wind Energy Program",
       "description": "Supports wind power development in India, creating clean energy and reducing carbon emissions.",
       "location": "India",
       "offset_potential_tons": 0.2,
       "category": "Renewable Energy - Wind",
       "benefits": ["Provides clean energy", "Reduces greenhouse gases", "Generates local employment"],
       "activities": ["Wind farm construction", "Energy production", "Community outreach"],
       "link": "https://www.goldstandard.org/projects/indian-wind-energy",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_IndianWind.jpg"
   },
   {
       "name": "Mangrove Restoration in Kenya",
       "description": "Rehabilitates coastal mangroves to increase CO2 absorption, protect marine biodiversity, and reduce erosion.",
       "location": "Kenya",
       "offset_potential_tons": 0.12,
       "category": "Reforestation",
       "benefits": ["Increases biodiversity", "Protects coastlines", "Sequesters CO2"],
       "activities": ["Planting mangroves", "Community involvement", "Erosion prevention"],
       "link": "https://www.ecosystemmarketplace.com/kenya-mangrove-restoration/",
       "image_url": "https://www.ecosystemmarketplace.com/images/kenya-mangroves.jpg"
   },
      {
       "name": "Biogas Support Program in Nepal",
       "description": "Provides rural households with biogas systems, turning organic waste into a clean fuel source and reducing firewood use.",
       "location": "Nepal",
       "offset_potential_tons": 0.15,
       "category": "Biogas",
       "benefits": ["Reduces deforestation", "Improves air quality", "Provides a renewable energy source"],
       "activities": ["Biogas system installation", "Waste-to-energy training", "Support for local households"],
       "link": "https://www.goldstandard.org/projects/biogas-support-nepal",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_NepalBiogas.jpg"
   },
   {
       "name": "Kenya Reforestation Project",
       "description": "A community-led reforestation initiative in Kenya to combat desertification, restore biodiversity, and sequester carbon.",
       "location": "Kenya",
       "offset_potential_tons": 0.2,
       "category": "Reforestation",
       "benefits": ["Restores degraded land", "Provides local jobs", "Sequesters CO2"],
       "activities": ["Tree planting", "Community engagement", "Environmental education"],
       "link": "https://www.trees.org/our-work/kenya",
       "image_url": "https://www.trees.org/wp-content/uploads/2021/06/Kenya-Tree-Planting.jpg"
   },
   {
       "name": "Indonesia Peatland Restoration",
       "description": "Restores damaged peatlands to prevent CO2 release, increase biodiversity, and protect water quality.",
       "location": "Indonesia",
       "offset_potential_tons": 0.3,
       "category": "Peatland Restoration",
       "benefits": ["Protects water resources", "Preserves biodiversity", "Reduces CO2 emissions"],
       "activities": ["Peatland rewetting", "Community training", "Biodiversity protection"],
       "link": "https://www.unep.org/peatland-indonesia",
       "image_url": "https://www.unep.org/sites/default/files/styles/og_image/public/2021-07/peatland-restoration.jpg"
   },
   {
       "name": "Malawi Improved Forest Management",
       "description": "Encourages sustainable forestry in Malawi by providing alternatives to unsustainable tree harvesting.",
       "location": "Malawi",
       "offset_potential_tons": 0.12,
       "category": "Forest Management",
       "benefits": ["Reduces deforestation", "Promotes sustainable livelihoods", "Enhances biodiversity"],
       "activities": ["Forest monitoring", "Community outreach", "Sustainable harvesting"],
       "link": "https://carbonfund.org/project/forest-management-malawi/",
       "image_url": "https://carbonfund.org/wp-content/uploads/2020/03/forest-malawi.jpg"
   },
   {
       "name": "Honduras Hydroelectric Power Project",
       "description": "Develops small hydroelectric power plants in Honduras to provide renewable energy and reduce fossil fuel use.",
       "location": "Honduras",
       "offset_potential_tons": 0.25,
       "category": "Renewable Energy - Hydroelectric",
       "benefits": ["Provides clean energy", "Reduces CO2 emissions", "Supports local economy"],
       "activities": ["Hydro plant construction", "Energy distribution", "Local employment"],
       "link": "https://www.goldstandard.org/projects/honduras-hydro",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_HondurasHydro.jpg"
   },
   {
       "name": "Brazilian Cerrado Conservation",
       "description": "Protects Brazil's Cerrado savannah from agricultural expansion, preserving biodiversity and reducing CO2 emissions.",
       "location": "Brazil",
       "offset_potential_tons": 0.35,
       "category": "Conservation",
       "benefits": ["Preserves habitat", "Prevents carbon release", "Protects indigenous lands"],
       "activities": ["Land monitoring", "Community partnerships", "Sustainable farming practices"],
       "link": "https://www.conservation.org/projects/brazil-cerrado",
       "image_url": "https://www.conservation.org/images/default-source/default-album/cerrado.jpg"
   },
   {
       "name": "Thailand Biomass Energy Project",
       "description": "Converts agricultural waste into biomass energy, reducing methane emissions and providing clean energy.",
       "location": "Thailand",
       "offset_potential_tons": 0.18,
       "category": "Renewable Energy - Biomass",
       "benefits": ["Reduces methane emissions", "Provides renewable energy", "Supports local agriculture"],
       "activities": ["Biomass plant operation", "Agricultural waste collection", "Energy generation"],
       "link": "https://carbonfund.org/project/biomass-energy-thailand/",
       "image_url": "https://carbonfund.org/wp-content/uploads/2019/07/biomass-energy.jpg"
   },
   {
       "name": "Nicaragua Reforestation for Coffee Farmers",
       "description": "Promotes tree planting on coffee farms to sequester CO2 and create shaded, sustainable agriculture.",
       "location": "Nicaragua",
       "offset_potential_tons": 0.1,
       "category": "Agroforestry",
       "benefits": ["Increases farm productivity", "Sequesters CO2", "Improves soil quality"],
       "activities": ["Tree planting on farms", "Sustainable farming education", "Carbon monitoring"],
       "link": "https://www.treesforclimate.com/nicaragua-reforestation",
       "image_url": "https://www.treesforclimate.com/wp-content/uploads/2021/05/Nicaragua-coffee.jpg"
   },
   {
       "name": "Philippines Mangrove Conservation",
       "description": "Protects and restores mangrove forests in the Philippines, which absorb CO2 and provide storm protection.",
       "location": "Philippines",
       "offset_potential_tons": 0.2,
       "category": "Mangrove Conservation",
       "benefits": ["Prevents coastal erosion", "Increases biodiversity", "Sequesters CO2"],
       "activities": ["Mangrove planting", "Coastal monitoring", "Community participation"],
       "link": "https://www.mangroveproject.org/philippines",
       "image_url": "https://www.mangroveproject.org/wp-content/uploads/2019/02/mangroves.jpg"
   },
   {
       "name": "Cambodia Improved Cookstoves Program",
       "description": "Distributes efficient cookstoves to reduce wood fuel use and lower household emissions.",
       "location": "Cambodia",
       "offset_potential_tons": 0.08,
       "category": "Clean Cooking",
       "benefits": ["Improves air quality", "Reduces deforestation", "Increases fuel efficiency"],
       "activities": ["Cookstove distribution", "Training on usage", "Community outreach"],
       "link": "https://www.goldstandard.org/projects/cambodia-cookstoves",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_CambodiaCookstove.jpg"
   },
      {
       "name": "Uganda Safe Water Access Project",
       "description": "Provides communities in Uganda with access to safe drinking water, reducing the need for boiling water with firewood and lowering CO2 emissions.",
       "location": "Uganda",
       "offset_potential_tons": 0.1,
       "category": "Clean Water Access",
       "benefits": ["Reduces wood use", "Improves health", "Lowers CO2 emissions"],
       "activities": ["Well installation", "Water purification training", "Community health workshops"],
       "link": "https://www.cooleffect.org/project/uganda-safe-water-access",
       "image_url": "https://www.cooleffect.org/images/uganda-safe-water.jpg"
   },
   {
       "name": "Vietnam Wind Power Development",
       "description": "Develops wind power infrastructure in Vietnam to provide renewable energy and reduce reliance on fossil fuels.",
       "location": "Vietnam",
       "offset_potential_tons": 0.22,
       "category": "Renewable Energy - Wind",
       "benefits": ["Provides clean energy", "Reduces fossil fuel dependency", "Creates local jobs"],
       "activities": ["Wind turbine installation", "Energy grid integration", "Technical training"],
       "link": "https://www.goldstandard.org/projects/vietnam-wind-power",
       "image_url": "https://www.goldstandard.org/sites/default/files/styles/large/public/2019-02/GS_Project_VietnamWind.jpg"
   },
   {
       "name": "Pakistan Solar Energy Expansion",
       "description": "Expands solar power access in rural Pakistan, offering a renewable energy source and reducing CO2 emissions.",
       "location": "Pakistan",
       "offset_potential_tons": 0.14,
       "category": "Renewable Energy - Solar",
       "benefits": ["Reduces CO2 emissions", "Improves energy access", "Lowers electricity costs"],
       "activities": ["Solar panel installation", "Maintenance training", "Community outreach"],
       "link": "https://www.globalgiving.org/projects/pakistan-solar-energy/",
       "image_url": "https://www.globalgiving.org/images/pakistan-solar-project.jpg"
   },
   {
       "name": "Himalayan Sustainable Tourism",
       "description": "Promotes sustainable tourism in the Himalayan region, reducing environmental impact and supporting local economies.",
       "location": "Nepal & India",
       "offset_potential_tons": 0.09,
       "category": "Sustainable Tourism",
       "benefits": ["Protects natural resources", "Creates eco-friendly jobs", "Educates travelers"],
       "activities": ["Eco-tourism training", "Environmental awareness campaigns", "Community engagement"],
       "link": "https://www.himalayanecotourism.com",
       "image_url": "https://www.himalayanecotourism.com/images/himalayan-tourism.jpg"
   },
   {
       "name": "Mozambique Forest Conservation Project",
       "description": "Protects forest areas in Mozambique from deforestation, preserving habitats and sequestering CO2.",
       "location": "Mozambique",
       "offset_potential_tons": 0.28,
       "category": "Forest Conservation",
       "benefits": ["Preserves biodiversity", "Prevents deforestation", "Sequesters carbon"],
       "activities": ["Forest patrols", "Community-based conservation", "Biodiversity monitoring"],
       "link": "https://www.carbonneutral.com/mozambique-forest",
       "image_url": "https://www.carbonneutral.com/sites/default/files/styles/large/public/2019-02/mozambique-forest.jpg"
   }
   
]


# Function to add projects to the database
def add_projects():
    for project_data in carbon_offset_projects:
        project, created = CarbonOffsetProject.objects.get_or_create(
            name=project_data["name"],
            defaults={
                "description": project_data["description"],
                "location": project_data["location"],
                "offset_potential_tons": project_data["offset_potential_tons"],
                "category": project_data["category"],
                "benefits": project_data["benefits"],
                "activities": project_data["activities"],
                "link": project_data["link"],
                "image_url": project_data["image_url"]
            }
        )
        if created:
            print(f'Created project: {project.name}')
        else:
            print(f'Project already exists: {project.name}')

if __name__ == "__main__":
    add_projects()
    print("All projects have been added to the database.")