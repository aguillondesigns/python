class EngravingEstimator:
    # Custom Coasters
    numberCoasters = 0
    coasterFee = 5
    coasterHolderFee = 25
    coasterMinimumCharge = 30 # Design + engraving

    # Shot Glasses
    numberGlasses = 0
    glassFee = 7
    glassHolderFee = 35

    # Wallets
    numberWallets = 0
    walletFee = 35
    engravingFee = 5

    def GetCoasterEstimate(this, numberCoasters, includingHolder = True):
        coasterCost = this.coasterFee * numberCoasters
        holderCost = this.coasterHolderFee if includingHolder else 0
        return max(coasterCost + holderCost, this.coasterMinimumCharge)

    def GetShotglassEstimate(this, numberGlasses, includeHolder = True):
        glassesCost = this.glassFee * numberGlasses
        holderCost = this.glassHolderFee if includeHolder else 0
        return glassesCost + holderCost

    def GetWalletEstimate(this, numberWallets, engravingOption):
        engravingCost = this.engravingFee * engravingOption
        walletCost = engravingCost + this.walletFee
        return walletCost * numberWallets

estimator = EngravingEstimator()

# number coasters (4, 6, 8), holder
coasters, holder = 4, True
coasterEstimate = estimator.GetCoasterEstimate(coasters, holder)
print("Coaster Set Estimate:", coasterEstimate)

# number shot glasses (2 or 4, holder )
glasses, holder = 4, True
shotGlassEstimate = estimator.GetShotglassEstimate(glasses, holder)
print("Shot Glass Set Estimate:", shotGlassEstimate)

# number wallets, engraving 0, 1, 2  (0 = no engraving, 1 = 1 side, 2 = 2 sides)
numberWallets, sides = 3, 2
walletEstimate = estimator.GetWalletEstimate(numberWallets, sides)
print("Estimate for", numberWallets, "wallets:", walletEstimate)