package main

import (
    "encoding/json"
    "fmt"
    "github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type AssetTransferContract struct {
    contractapi.Contract
}

type Asset struct {
    ID    string `json:"ID"`
    Value string `json:"Value"`
}

func (c *AssetTransferContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
    assets := []Asset{{ID: "asset1", Value: "100"}, {ID: "asset2", Value: "200"}}
    for _, asset := range assets {
        assetJSON, _ := json.Marshal(asset)
        _ = ctx.GetStub().PutState(asset.ID, assetJSON)
    }
    return nil
}

func (c *AssetTransferContract) CreateAsset(ctx contractapi.TransactionContextInterface, id, value string) error {
    exists, _ := c.AssetExists(ctx, id)
    if exists {
        return fmt.Errorf("asset %s already exists", id)
    }
    asset := Asset{ID: id, Value: value}
    assetJSON, _ := json.Marshal(asset)
    return ctx.GetStub().PutState(id, assetJSON)
}

func (c *AssetTransferContract) ReadAsset(ctx contractapi.TransactionContextInterface, id string) (*Asset, error) {
    assetJSON, err := ctx.GetStub().GetState(id)
    if err != nil || assetJSON == nil {
        return nil, fmt.Errorf("asset %s does not exist", id)
    }
    var asset Asset
    _ = json.Unmarshal(assetJSON, &asset)
    return &asset, nil
}

func (c *AssetTransferContract) AssetExists(ctx contractapi.TransactionContextInterface, id string) (bool, error) {
    assetJSON, _ := ctx.GetStub().GetState(id)
    return assetJSON != nil, nil
}

func main() {
    chaincode, _ := contractapi.NewChaincode(&AssetTransferContract{})
    _ = chaincode.Start()
}
