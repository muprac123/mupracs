// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract DataMarketplace {
    struct Listing {
        address payable seller;
        string dataCID;
        uint256 price;
        bool sold;
    }
    Listing[] public listings;
    event DataListed(uint256 listingId, address indexed seller, string dataCID, uint256 price);
    event DataPurchased(uint256 listingId, address indexed buyer, uint256 price);
    function listData(string memory _dataCID, uint256 _price) public {
        require(_price > 0, "Price must be positive");
        listings.push(Listing(payable(msg.sender), _dataCID, _price, false));
        emit DataListed(listings.length - 1, msg.sender, _dataCID, _price);
    }
    function buyData(uint256 listingId) public payable {
        Listing storage listing = listings[listingId];
        require(!listing.sold, "Already sold");
        require(msg.value == listing.price, "Incorrect payment");
        listing.sold = true;
        listing.seller.transfer(msg.value);
        emit DataPurchased(listingId, msg.sender, msg.value);
    }
    function getListing(uint256 listingId) public view returns (address, string memory, uint256, bool) {
        Listing storage listing = listings[listingId];
        return (listing.seller, listing.dataCID, listing.price, listing.sold);
    }
}
