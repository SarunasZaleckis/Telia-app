from fastapi import FastAPI
import service_order as payload
import os

if __name__ == '__main__':
    print('Starting TMF Application')
    
    # Not used
    originUrl = os.environ['ORIGIN_URL']
    
    app = FastAPI()
    
    @app.post("/acceptServiceOrder")
    async def acceptServiceOrder(data):
        processServiceOrder(data)
        
    def processServiceOrder(data):
        print("Processing Service Order")
        if validateServiceOrder(data):
            data = payload.ServiceOrder(**data)
            acknowledgeServiceOrder(data)
            
            inProgressOrder(data)
        else:
            rejectServiceOrder(data=data)
        
    def inProgressOrder(data):
        print('Set to to "In Progress", notify origin and continue processing')
        notifyServiceOrderStatus(data=data, state="in progress")
        
        # This is incorrect, there should be additional logic to determine the actual state of the ServiceOrder OrderItems if these have the neccessary data
        # Additionally missing Cancel logic for returned ServiceOrder
        match data.state:
            case 'Pending':
                print('Store data locally, notify origin of missing OrderItem data')
                notifyServiceOrderStatus(data=data, state='pending')
            case 'Held':
                print('Store data locally, notify origin of order fall-out await resolution event')
                notifyServiceOrderStatus(data=data, state='held')
        
        print('No issues found, continue processing')
        
        try:
            completeServiceOrder(data=data)
        except PartialCompletion:
            partialServiceOrder(data=data)
        except:
            failServiceOrder(data=data)

    def continueProcessingOrder(data):
        print('Retrieve stored ServiceOrder')
    
    def notifyServiceOrderStatus(data, state):
        print('Notifies origin of new state')
    
    def rejectServiceOrder(data):
        print('Set the state to "Rejected" and return ServiceOrder')
        notifyServiceOrderStatus(data=data, state="rejected")
        
    def acknowledgeServiceOrder(data):
        print('Set the state to "Acknowledged", notify the ServiceOrder origin of the changed state')
        notifyServiceOrderStatus(data=data, state="acknowledged")
        
    def cancelServiceOrder(data):
        print('Set state to "Cancelled" and return')
        notifyServiceOrderStatus(data=data, state="cancelled")
    
    def completeServiceOrder(data):
        print('Finalize ServiceOrder execution, if method fails returns Generic Execption or PartialCompletion, otherwise completes successfully')
        
        # Again, requires additional logic to define when and where to fail exactly with which type of Exception
        match data.state:
            case 'completed':
                notifyServiceOrderStatus(data=data, state="completed")
                return
            case 'partial':
                raise PartialCompletion(Exception('Partial completion'))
            case 'failed':
                raise Exception('Broke at the wrong place')

    def failServiceOrder(data):
        print('Set the state to "Failed" and return back the Service Order with the modified state')
        notifyServiceOrderStatus(data=data, state="failed")
        
    def partialServiceOrder(data):
        print('Partially executed')
        notifyServiceOrderStatus(data=data, state="partial")
        
    def validateServiceOrder(data) -> None:
        try:
            payload.ServiceOrder(**data)
        except:
            rejectServiceOrder(data)
            return False
            
        return True
    
class PartialCompletion(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

