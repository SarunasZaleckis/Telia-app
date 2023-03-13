from pydantic import BaseModel, validator, root_validator
import typing


class ServiceOrder(BaseModel):
    id: str
    href: str
    externalId: str
    priority: str
    description: str
    category: str
    state: str
    orderDate: str
    completionDate: str
    requestedStartDate: str
    requestedCompletionDate: str
    expectedCompletionDate: str
    startDate: str
    type: str
    note: typing.List["note"]
    relatedParty: typing.List["relatedParty"]
    orderItem: typing.List["orderItem"]

class note(BaseModel):
    date: str
    author: str
    text: str

class relatedParty(BaseModel):
    id: str
    href: str
    role: str
    name: str
    refferedType: str

class orderItem(BaseModel):
    id: str
    action: str
    state: str
    service: "service"
        
class service(BaseModel):
    type: str
    schemaLocation: str
    state: str
    serviceType: str
    serviceCharacteristic: typing.List["serviceCharacteristic"]
            
class serviceCharacteristic(BaseModel):
    name: str
    valueType: str
    value: "value"
        
class value(BaseModel):
    type: str
    schemaLocation: str
    vCPE_IP: str
    
class serviceSpecification(BaseModel):
    type: str
    schemaLocation: str
    id: str
    href: str
    name: str
    version: str
    invariantUUID: str
    toscaModelIURL: str
    targetServiceSchema: "targetServiceSchema"
    
class targetServiceSchema(BaseModel):
    type: str
    schemaLocation: str
