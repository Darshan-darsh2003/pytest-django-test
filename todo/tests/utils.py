import random

class MockRequests:
    def create_random_task(self):
        titles = ['Buy groceries', 'Clean the house', 'Do laundry', 'Cook dinner', 'Walk the dog', 'Wash the car', 'Mow the lawn', 'Take out the trash', 'Vacuum the house', 'Wash the dishes',
                    'Make the bed', 'Sweep the floor', 'Dust the furniture', 'Organize the closet', 'Water the plants', 'Feed the pets', 'Clean the bathroom', 'Clean the kitchen', 'Clean the bedroom',
                    'Clean the living room', 'Clean the dining room', 'Clean the basement', 'Clean the attic', 'Clean the garage', 'Clean the porch', 'Clean the patio', 'Clean the deck', 'Clean the driveway',
                    'Clean the sidewalk', 'Clean the windows', 'Clean the gutters', 'Clean the roof', 'Clean the chimney', 'Clean the fireplace', 'Clean the stove', 'Clean the oven', 'Clean the microwave',
                    'Clean the refrigerator', 'Clean the freezer', 'Clean the pantry', 'Clean the cabinets', 'Clean the drawers', 'Clean the countertops', 'Clean the sink', 'Clean the faucet', 'Clean the dishwasher',
                    'Clean the washing machine', 'Clean the dryer', 'Clean the shower', 'Clean the bathtub', 'Clean the toilet', 'Clean the sink', 'Clean the mirror', 'Clean the medicine cabinet', 'Clean the towel rack',
                    'Clean the toilet paper holder', 'Clean the shower curtain', 'Clean the shower rod', 'Clean the shower head', 'Clean the light fixtures', 'Clean the exhaust fan', 'Clean the floor', 'Clean the walls',
                    'Clean the ceiling', 'Clean the door', 'Clean the door frame', 'Clean the door knob', 'Clean the door hinges', 'Clean the door stop', 'Clean the doorbell', 'Clean the windowsill', 'Clean the baseboards',
                    'Clean the crown molding', 'Clean the chair rail', 'Clean the wainscoting', 'Clean the picture frames', 'Clean the wall hangings', 'Clean the wall shelves', 'Clean the wall hooks', 'Clean the wall clock',
                    'Clean the wall thermostat', 'Clean the wall outlets', 'Clean the wall switches', 'Clean the wall plates', 'Clean the wall vents', 'Clean the wall registers', 'Clean the wall heater', 'Clean the wall air conditioner',
                    'Clean the wall fan', 'Clean the wall speakers', 'Clean the wall TV', 'Clean the wall computer', 'Clean the wall phone', 'Clean the wall charger', 'Clean the wall remote', 'Clean the wall clock', 'Clean the wall calendar',
                    'Clean the wall art', 'Clean the wall decor', 'Clean the wall paint', 'Clean the wall wallpaper', 'Clean the wall paneling', 'Clean the wall trim', 'Clean the wall molding', 'Clean the wall insulation', 'Clean the wall studs',
                    'Clean the wall drywall', 'Clean the wall plaster', 'Clean the wall brick', 'Clean the wall stone', 'Clean the wall tile', 'Clean the wall grout', 'Clean the wall caulk', 'Clean the wall sealant', 'Clean the wall adhesive',
                    'Clean the wall screws', 'Clean the wall nails', 'Clean the wall anchors', 'Clean the wall hooks', 'Clean the wall brackets', 'Clean the wall shelves', 'Clean the wall cabinets', 'Clean the wall drawers', 'Clean the wall desk',
                ]  
        descriptions = ['Buy groceries for the week', 'Clean the house from top to bottom', 'Do laundry for the whole family', 'Cook dinner for the whole family', 'Walk the dog around the block', 'Wash the car inside and out', 'Mow the lawn front and back', 'Take out the trash from the kitchen', 'Vacuum the house from top to bottom', 'Wash the dishes from breakfast',
                        'Make the bed in the master bedroom', 'Sweep the floor in the living room', 'Dust the furniture in the dining room', 'Organize the closet in the master bedroom', 'Water the plants in the living room', 'Feed the pets in the kitchen', 'Clean the bathroom from top to bottom', 'Clean the kitchen from top to bottom', 'Clean the bedroom from top to bottom',
                        'Clean the living room from top to bottom', 'Clean the dining room from top to bottom', 'Clean the basement from top to bottom', 'Clean the attic from top to bottom', 'Clean the garage from top to bottom', 'Clean the porch from top to bottom', 'Clean the patio from top to bottom', 'Clean the deck from top to bottom', 'Clean the driveway from top to bottom',
                        'Clean the sidewalk from top to bottom', 'Clean the windows from top to bottom', 'Clean the gutters from top to bottom', 'Clean the roof from top to bottom', 'Clean the chimney from top to bottom', 'Clean the fireplace from top to bottom', 'Clean the stove from top to bottom', 'Clean the oven from top to bottom', 'Clean the microwave from top to bottom',
                        'Clean the refrigerator from top to bottom', 'Clean the freezer from top to bottom', 'Clean the pantry from top to bottom', 'Clean the cabinets from top to bottom', 'Clean the drawers from top to bottom', 'Clean the countertops from top to bottom', 'Clean the sink from top to bottom', 'Clean the faucet from top to bottom', 'Clean the dishwasher from top to bottom',
                        'Clean the washing machine from top to bottom', 'Clean the dryer from top to bottom', 'Clean the shower from top to bottom', 'Clean the bathtub from top to bottom', 'Clean the toilet from top to bottom', 'Clean the sink from top to bottom', 'Clean the mirror from top to bottom', 'Clean the medicine cabinet from top to bottom', 'Clean the towel rack from top to bottom',
                        'Clean the toilet paper holder from top to bottom', 'Clean the shower curtain from top to bottom', 'Clean the shower rod from top to bottom', 'Clean the shower head from top to bottom', 'Clean the light fixtures from top to bottom', 'Clean the exhaust fan from top to bottom', 'Clean the floor from top to bottom', 'Clean the walls from top to bottom',
                        'Clean the ceiling from top to bottom', 'Clean the door from top to bottom', 'Clean the door frame from top to bottom', 'Clean the door knob from top to bottom', 'Clean the door hinges from top to bottom', 'Clean the door stop from top to bottom', 'Clean the doorbell from top to bottom', 'Clean the windowsill from top to bottom', 'Clean the baseboards from top to bottom',
                        'Clean the crown molding from top to bottom', 'Clean the chair rail from top to bottom', 'Clean the wainscoting from top to bottom', 'Clean the picture frames from top to bottom', 'Clean the wall hangings from top to bottom', 'Clean the wall shelves from top to bottom', 'Clean the wall hooks from top to bottom', 'Clean the wall clock from top to bottom',
                        'Clean the wall thermostat from top to bottom', 'Clean the wall outlets from top to bottom', 'Clean the wall switches from top to bottom', 'Clean the wall plates from top to bottom', 'Clean the wall vents from top to bottom', 'Clean the wall registers from top to bottom', 'Clean the wall heater from top to bottom', 'Clean the wall air conditioner from top to bottom',
                        'Clean the wall fan from top to bottom', 'Clean the wall speakers from top to bottom', 'Clean the wall TV from top to bottom', 'Clean the wall computer from top to bottom', 'Clean the wall phone from top to bottom', 'Clean the wall charger from top to bottom', 'Clean the wall remote from top to bottom', 'Clean the wall clock from top to bottom', 'Clean the wall calendar from top to bottom',
                        'Clean the wall art from top to bottom', 'Clean the wall decor from top to bottom', 'Clean the wall paint from top to bottom', 'Clean the wall wallpaper from top to bottom', 'Clean the wall paneling from top to bottom', 'Clean the wall trim from top to bottom', 'Clean the wall molding from top to bottom', 'Clean the wall insulation from top to bottom', 'Clean the wall studs from top to bottom',
                        'Clean the wall drywall from top to bottom', 'Clean the wall plaster from top to bottom', 'Clean the wall brick from top to bottom', 'Clean the wall stone from top to bottom', 'Clean the wall tile from top to bottom', 'Clean the wall grout from top to bottom', 'Clean the wall caulk from top to bottom', 'Clean the wall sealant from top to bottom', 'Clean the wall adhesive from top to bottom',
                        'Clean the wall screws from top to bottom', 'Clean the wall nails from top to bottom', 'Clean the wall anchors from top to bottom', 'Clean the wall hooks from top to bottom', 'Clean the wall brackets from top to bottom', 'Clean the wall shelves from top to bottom', 'Clean the wall cabinets from top to bottom', 'Clean the wall drawers from top to bottom', 'Clean the wall desk from top to bottom',
                        ]
        
        tasks = []
        
        for i in range(len(titles)):
            task = {}
            task['title'] = titles[i]
            task['description'] = descriptions[i]
            task['user_id'] = 1
            tasks.append(task)
        
        task = random.choice(tasks)
        task['user_id'] = 1
        
        return task