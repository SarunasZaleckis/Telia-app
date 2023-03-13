from fastapi import FastAPI
import json
import service_order as payload

if __name__ == '__main__':
    print('Starting TMF Application')

    app = FastAPI()
    
    @app.post("/acceptServiceOrder")
    async def acceptServiceOrder(data):
        processServiceOrder(data)
        
    def processServiceOrder(data):
        print("Processing Service Order")
        if validateServiceOrder(data):
            acknowledgeServiceOrder()
            
            inProgressOrder(data)
        
    def inProgressOrder(data):
        print("Doing something fancy")

    def notifyServiceOrderStatus(state):
        print('placeholder')

    def processServiceOrder():
        print('placeholder')
    
    def rejectServiceOrder(data):
        print("Placeholder")
        
    def acknowledgeServiceOrder():
        print()
        
    def cancelServiceOrder():
        print()
    
    def completeServiceOrder():
        print()
        
    def failServiceOrder(data):
        print
        
    def partialServiceOrder():
        print
        
    def validateServiceOrder(data) -> bool:
        try:
            payload.ServiceOrder(**data)
        except:
            rejectServiceOrder(data)
            return False
            
        return True
