from decimal import Decimal
from typing import NamedTuple
from pyserum import market
from pyserum.market.state import MarketState
from solana.publickey import PublicKey

import datetime
import mango


def fake_public_key() -> PublicKey:
    return PublicKey("11111111111111111111111111111112")


def fake_seeded_public_key(seed: str) -> PublicKey:
    return PublicKey.create_with_seed(PublicKey("11111111111111111111111111111112"), seed, PublicKey("11111111111111111111111111111111"))


def fake_account_info(address: PublicKey = fake_public_key(), executable: bool = False, lamports: Decimal = Decimal(0), owner: PublicKey = fake_public_key(), rent_epoch: Decimal = Decimal(0), data: bytes = bytes([0])):
    return mango.AccountInfo(address, executable, lamports, owner, rent_epoch, data)


def fake_token() -> mango.Token:
    return mango.Token("FAKE", "Fake Token", fake_seeded_public_key("fake token"), Decimal(6))


def fake_context() -> mango.Context:
    return mango.Context("fake-cluster", "https://fake-cluster-host", fake_seeded_public_key("program ID"), fake_seeded_public_key("DEX program ID"), "FAKE_GROUP", fake_seeded_public_key("group ID"))


def fake_index() -> mango.Index:
    token = fake_token()
    borrow = mango.TokenValue(token, Decimal(0))
    deposit = mango.TokenValue(token, Decimal(0))
    return mango.Index(mango.Version.V1, token, datetime.datetime.now(), borrow, deposit)


def fake_market() -> market.Market:
    Container = NamedTuple("Container", [("own_address", PublicKey), ("vault_signer_nonce", int)])
    container = Container(own_address=fake_seeded_public_key("market address"), vault_signer_nonce=2)
    state = MarketState(container, fake_seeded_public_key("program ID"), 6, 6)
    return market.Market(None, state)
