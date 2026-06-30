| Field | Requirement |
|---|---|
| ID | TC-BT-### |
| Title | Short |
| Preconditions | Data, role, feature flags |
| Steps | Numbered, atomic |
| Expected result | Observable |
| Priority | P1–P3 with one-line risk reason |
| Traceability | Which AC line |


-----
### TC-BT-001 — [Positive] Create wishlist with valid name
**Preconditions:** User is signed in (valid bearer token); user has fewer than 10 existing wishlists.
**Steps:**
1. Send `POST /wishlists` with `name = "Summer Reads"`.
**Expected result:** Response is `201 Created`; response body contains the new wishlist with `name = "Summer Reads"` and a generated `wishlist_id`.
**Priority:** P1 — core creation flow; if broken, no wishlists can be made.
**Traceability:** AC1

----
### TC-BT-002 — [Positive] Add book to wishlist up to limit boundary (50 books)
**Preconditions:** User is signed in; user owns a wishlist containing exactly 49 distinct `book_id`s.
**Steps:**
1. Send `POST /wishlists/{wishlist_id}/books` with a 50th distinct valid `book_id`.
**Expected result:** Response is `201 Created`; wishlist now contains 50 books; subsequent `GET /wishlists/{wishlist_id}` returns `book_count: 50`.
**Priority:** P1 — boundary case for the documented 50-book limit; off-by-one errors here are common.
**Traceability:** AC3

----
## TC-BT-005 — [Negative] Reject 51st book with WL_FULL
**Preconditions:** User is signed in; user owns a wishlist already containing 50 distinct books.
**Steps:**
1. Send `POST /wishlists/{wishlist_id}/books` with a new, valid, distinct `book_id`.
**Expected result:** Response is `409 Conflict` (or equivalent); response body `error: "WL_FULL"`; wishlist book count remains 50 (verify via `GET /wishlists/{wishlist_id}`).
**Priority:** P1 — direct test of the documented limit enforcement; failure means unbounded wishlist growth.
**Traceability:** AC3
-----

### TC-BT-003 — [Positive] Remove a book that still exists in the catalog
**Preconditions:** User is signed in; user owns a wishlist containing a book with `book_id = X`, which still exists in the catalog.
**Steps:**
1. Send `DELETE /wishlists/{wishlist_id}/books/{X}`.
**Expected result:** Response is `200 OK` (or `204 No Content`); subsequent `GET /wishlists/{wishlist_id}` no longer lists `book_id = X`.
**Priority:** P2 — standard remove path, lower risk than limit/auth edge cases.
**Traceability:** AC4
---
 
### TC-BT-004 — [Negative] Reject empty name after trimming whitespace
**Preconditions:** User is signed in.
**Steps:**
1. Send `POST /wishlists` with `name = "   "` (whitespace only).
**Expected result:** Response is `400 Bad Request`; response body contains a validation error indicating the name is empty after trimming (e.g. `error: "WL_INVALID_NAME"`); no wishlist is created (confirm via `GET /wishlists` count unchanged).
**Priority:** P1 — invalid-data guard required directly by AC1; silent acceptance would corrupt data.
**Traceability:** AC1
---

### TC-BT-006 — [Negative] Reject duplicate case-insensitive wishlist name
**Preconditions:** User is signed in; user already owns a wishlist named `"Beach Reads"`.
**Steps:**
1. Send `POST /wishlists` with `name = "beach reads"` (different case, same user).
**Expected result:** Response is `409 Conflict`; response body `error: "WL_DUP_NAME"`; no second wishlist is created (confirm via `GET /wishlists` count unchanged for that name).
**Priority:** P1 — explicit AC requirement; case-sensitivity bugs are a common slip.
**Traceability:** AC2
---
 
### TC-BT-007 — [Negative] Other authenticated user cannot view another user's wishlist (no enumeration)
**Preconditions:** Two signed-in users exist, User A and User B; User A owns wishlist `wishlist_id = W1`; test is run with User B's bearer token.
**Steps:**
1. Send `GET /wishlists/W1` using User B's bearer token.
**Expected result:** Response is `404 Not Found` (not `403 Forbidden`, to avoid confirming the wishlist's existence); response body does not contain any wishlist data (name, book list, owner).
**Priority:** P1 — security/authorization control; failure leaks data ownership and violates AC5 directly.
**Traceability:** AC5
---